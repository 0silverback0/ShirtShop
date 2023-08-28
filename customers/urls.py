from django.urls import path
from . import views
# from .views import 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('token-auth/', obtain_auth_token),
    path('items/<int:pk>', views.SingleProductView.as_view(), name='single-item'),
    path('items/<int:product_id>/user/<int:user_id>/add-to-cart', views.AddToCartView.as_view(), name='add-to-cart'),
    path('users/<int:user_id>/cart/', views.UserCartView.as_view(), name='user-cart'),
    path('place-order/<int:user_id>/', views.CartToOrderView.as_view(), name='place-order'),
    path('cart-item/<int:cart_item_id>/delete/', views.DeleteCartItemView.as_view(), name='delete-cart-item'),
    path('cart-item/<int:cart_item_id>/subtract-quantity/', views.SubtractCartItemQuantityView.as_view(), name='subtract-cart-item-quantity'),
]