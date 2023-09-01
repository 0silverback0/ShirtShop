from django.test import TestCase
from products.models import Product
from rest_framework.test import APIClient
from rest_framework import status
from products.serializers import ProductSerializer
from django.contrib.auth.models import User, Group


class ProductItemTest(TestCase):
    """Test case for the Product model method get_item"""
    def test_get_item(self):
        item = Product.objects.create(name="test shirt", description='a test shirt', price=9, image_url='testimage.png', inventory=10)
        self.assertEqual(item.get_item(), "test shirt")

class ProductListViewTests(TestCase):
    """Test case for the ProductListView"""
    def setUp(self):
        # Create a test user with manager permissions 
        self.client = APIClient()

        # Create sample products
        Product.objects.create(name='Product 1', description='Description 1', price=10.0, image_url='image1.png', inventory=50)
        Product.objects.create(name='Product 2', description='Description 2', price=15.0, image_url='image2.png', inventory=30)

    def tearDown(self):
        """Clean up any created objects after the test"""
        User.objects.all().delete()
        Product.objects.all().delete()

    def test_product_list_view(self):
        """test for proper product data entry"""
        response = self.client.get('/products/items/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Deserialize the response data 
        serializer = ProductSerializer(Product.objects.all(), many=True)

        self.assertEqual(response.data, serializer.data)

        # Create a manager and assign them to the "manager" group
        manager_user = User.objects.create_user(username='manager', password='managerpassword')
        manager_group, created = Group.objects.get_or_create(name='manager')
        manager_user.groups.add(manager_group)

        # Simulate authentication for the manager user
        self.client.force_authenticate(user=manager_user)

        data = {
            'name': 'New Product',
            'description': 'Description for New Product',
            'price': '25.0',
            'image_url': 'new_image.png',
            'inventory': 100
        }

        response = self.client.post('/products/items/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the product was correctly stored in the database
        new_product = Product.objects.get(name='New Product')
        self.assertEqual(new_product.get_item(), 'New Product')

        # Check if the created product matches the provided data
        created_product = Product.objects.get(name='New Product')
        self.assertEqual(created_product.name, 'New Product')
        self.assertEqual(created_product.description, 'Description for New Product')
        self.assertEqual(str(created_product.price), '25.00')
        self.assertEqual(created_product.image_url, 'new_image.png')
        self.assertEqual(created_product.inventory, 100)
        
    def test_create_product_invalid_data(self):
        # Data with missing required fields
        data = {
            'name': 'New Product',
            'price': '25.0',
        }

        # Simulate a POST request with invalid data
        response = self.client.post('/products/items/', data, format='json')

        # Check if the response status code is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
