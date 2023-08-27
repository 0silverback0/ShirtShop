from django.urls import path
from . import views
# from .views import 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     path('token-auth/', obtain_auth_token),
    path('items/<int:pk>', views.SingleProductView.as_view(), name='single-item'),
    path('items/<int:product_id>/user/<int:user_id>/add-to-cart', views.AddToCartView.as_view(), name='add-to-cart'),
    path('users/<int:user_id>/cart/', views.UserCartView.as_view(), name='user-cart'),
]