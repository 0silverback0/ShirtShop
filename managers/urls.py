from django.urls import path
from . import views
from djoser.views import UserViewSet

urlpatterns = [
     path('api/auth/users/', UserViewSet.as_view({'get': 'retrieve'}), name='user-detail'),
     path('orders/<int:pk>', views.OrderViewSet.as_view(), name='orders'),
#  path('orders/<int:pk>', views.OrderListView.as_view(), name='orders')
]
