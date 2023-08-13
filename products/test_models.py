from django.test import TestCase
from products.models import Product
# from rest_framework.test import APIClient
from rest_framework import status
from products.serializers import ProductSerializer
from django.contrib.auth.models import User

#TestCase class
class ProductItemTest(TestCase):
    def test_get_item(self):
        item = Product.objects.create(name="test shirt", description='a test shirt', price=9, image_url='testimage.png', inventory=10)
        self.assertEqual(item.get_item(), "test shirt")
