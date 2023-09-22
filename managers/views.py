from products.views import IsManagerOrReadOnly
from customers.models import Order
from customers.serializers import OrderSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.


class OrderViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsManagerOrReadOnly]