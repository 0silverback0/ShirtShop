from django.urls import path
from . import views 

urlpatterns = [
    path('items/', views.ProductListView.as_view(), name='products-list'),
    path('items/<int:pk>/', views.ProductSingleView.as_view(), name='products'),

]