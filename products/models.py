from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.TextField()
    inventory = models.IntegerField(default=0)
    # featured = models.BooleanField(default=False)
    feature = models.BooleanField(default=False)

    def get_item(self):
        return self.name
