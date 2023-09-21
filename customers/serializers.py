from rest_framework import serializers
from .models import CartItem, Order, OrderItem
from rest_framework import serializers

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')  # Include the product name
    image_url = serializers.ReadOnlyField(source='product.image_url')
    
    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity', 'product_name', 'image_url')

# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = ('product', 'quantity')

# class OrderSerializer(serializers.ModelSerializer):
#     # order_items = OrderItemSerializer(many=True, read_only=True)

#     class Meta:
#         model = Order
#         fields = ('id', 'user', 'order_date', 'total_price', 'order_items')

# from rest_framework import serializers

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity', 'subtotal')

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'order_date', 'total_price', 'order_items')

# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User

class CustomAuthTokenSerializer(serializers.Serializer):
    token = serializers.CharField()
    user_id = serializers.IntegerField()
    username = serializers.CharField()
    # Add more user data fields as needed

    def create(self, validated_data):
        # The create method is not used for the Token model, so it can be empty
        pass

    def update(self, instance, validated_data):
        # The update method is not used for the Token model, so it can be empty
        pass
