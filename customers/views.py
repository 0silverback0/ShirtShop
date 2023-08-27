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