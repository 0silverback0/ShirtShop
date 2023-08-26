from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
# from .views import ProductListView
from . import views 

urlpatterns = [
    path('items', views.ProductListView.as_view(), name='products-list'),
    path('items/<int:pk>', views.ProductSingleView.as_view(), name='products'),

]