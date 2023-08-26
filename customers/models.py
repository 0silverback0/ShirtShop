from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# class Users(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=16)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

@receiver(post_save, sender=User)
def create_cart_for_user(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)

post_save.connect(create_cart_for_user, sender=User)
