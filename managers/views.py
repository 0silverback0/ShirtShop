from django.shortcuts import render
from products.views import IsManagerOrReadOnly
from customers.models import Order
from customers.serializers import OrderSerializer
from rest_framework import viewsets, permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# Create your views here.


class OrderViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsManagerOrReadOnly]  # Apply the custom permission class