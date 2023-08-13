from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# from .views import ProductListView
from . import views 

urlpatterns = [
    path('items', views.ProductListView.as_view(), name='products-list')
]