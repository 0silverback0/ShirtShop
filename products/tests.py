from django.test import TestCase
from products.models import Product
from rest_framework.test import APIClient
from rest_framework import status
from products.serializers import ProductSerializer
from django.contrib.auth.models import User


#TestCase class
class ProductItemTest(TestCase):
    def test_get_item(self):
        item = Product.objects.create(name="test shirt", description='a test shirt', price=9, image_url='testimage.png', inventory=10)
        self.assertEqual(item.get_item(), "test shirt")

class ProductListViewTests(TestCase):
    def setUp(self):
        # Create a test user with manager permissions (you can adjust this based on your authentication setup)
        self.client = APIClient()

        # Create some sample products in the database
        Product.objects.create(name='Product 1', description='Description 1', price=10.0, image_url='image1.png', inventory=50)
        Product.objects.create(name='Product 2', description='Description 2', price=15.0, image_url='image2.png', inventory=30)

    def test_product_list_view(self):
        # Simulate a GET request to the ProductListView
        response = self.client.get('/products/items/')

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Deserialize the response data using your ProductSerializer
        serializer = ProductSerializer(Product.objects.all(), many=True)

        # Check if the response data matches the serialized data
        self.assertEqual(response.data, serializer.data)


