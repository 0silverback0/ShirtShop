from django.shortcuts import render
from rest_framework import generics
from .models import Product, CartItem
from products.serializers import ProductSerializer
from django.contrib.auth.models import User

# Create your views here.

class SingleProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status

class AddToCartView(APIView):
    def post(self, request, user_id, product_id):
        try:
            # Retrieve the user (replace User with your user model)
            user = get_object_or_404(User, id=user_id)

            # Retrieve the product
            product = get_object_or_404(Product, id=product_id)

            # Try to get the cart item for this product in the user's cart
            cart_item = CartItem.objects.filter(cart=user.cart, product=product).first()

            if cart_item:
                # If the product is already in the cart, update the quantity
                cart_item.quantity += 1
                cart_item.save()
            else:
                # If the product is not in the cart, create a new cart item with quantity 1
                CartItem.objects.create(cart=user.cart, product=product, quantity=1)

            return JsonResponse({"message": "Product added to the cart"}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return JsonResponse({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Product.DoesNotExist:
            return JsonResponse({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

from rest_framework.response import Response
from .serializers import CartItemSerializer

class UserCartView(APIView):
    def get(self, request, user_id):
        # Retrieve the user's cart
        user = get_object_or_404(User, id=user_id)
        cart_items = CartItem.objects.filter(cart=user.cart)
        
        # Serialize the cart items
        serializer = CartItemSerializer(cart_items, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # ORDERS

    from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cart, CartItem, Order, OrderItem
from .serializers import OrderSerializer

class CartToOrderView(APIView):
    def post(self, request, user_id):
        try:
            # Retrieve the user's cart
            cart = Cart.objects.get(user_id=user_id)

            # Create a new order for the user
            order = Order.objects.create(user=cart.user)

            # Initialize total price to 0
            total_price = 0

            # Loop through cart items and create order items
            for cart_item in CartItem.objects.filter(cart=cart):
                order_item = OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity
                )

                # Add the subtotal of this order item to the total price
                total_price += order_item.subtotal()

                # Optionally, you can remove the cart item after adding it to the order
                cart_item.delete()

            # Set the calculated total price for the order
            order.total_price = total_price  # Set the total price here
            order.save()

            # You can serialize and return the order if needed
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Cart.DoesNotExist:
            return Response({"message": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
