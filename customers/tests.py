from django.test import TestCase
from django.contrib.auth.models import User, Group
from .models import Product, Cart, CartItem, Order, OrderItem

class ModelsTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create some products
        self.product1 = Product.objects.create(name='Product 1', price=10.0, inventory=50)
        self.product2 = Product.objects.create(name='Product 2', price=15.0, inventory=30)

        # Create a cart for the user
        self.cart = self.user.cart

    def test_cart_creation(self):
        # Check if the cart was created correctly
        self.assertEqual(self.cart.user, self.user)

    def test_cart_item_creation(self):
        # Create cart items
        cart_item1 = CartItem.objects.create(cart=self.cart, product=self.product1, quantity=2)
        cart_item2 = CartItem.objects.create(cart=self.cart, product=self.product2, quantity=3)

        # Check if cart items were created correctly
        self.assertEqual(cart_item1.cart, self.cart)
        self.assertEqual(cart_item2.cart, self.cart)
        self.assertEqual(cart_item1.product, self.product1)
        self.assertEqual(cart_item2.product, self.product2)
        self.assertEqual(cart_item1.quantity, 2)
        self.assertEqual(cart_item2.quantity, 3)

    def test_order_creation(self):
        # Create an order for the user
        order = Order.objects.create(user=self.user)

        # Check if the order was created correctly
        self.assertEqual(order.user, self.user)

    def test_order_item_creation(self):
        # Create an order for the user
        order = Order.objects.create(user=self.user)

        # Create order items
        order_item1 = OrderItem.objects.create(order=order, product=self.product1, quantity=2)
        order_item2 = OrderItem.objects.create(order=order, product=self.product2, quantity=3)

        # Check if order items were created correctly
        self.assertEqual(order_item1.order, order)
        self.assertEqual(order_item2.order, order)
        self.assertEqual(order_item1.product, self.product1)
        self.assertEqual(order_item2.product, self.product2)
        self.assertEqual(order_item1.quantity, 2)
        self.assertEqual(order_item2.quantity, 3)


    def test_user_created_cart(self):
        # Check if a user has a cart created automatically
        self.assertEqual(self.user.cart.user, self.user)

    def test_user_added_to_customer_group(self):
        # Check if a user is added to the 'customers' group
        customer_group = Group.objects.get(name='customers')
        self.assertTrue(self.user.groups.filter(pk=customer_group.pk).exists())
