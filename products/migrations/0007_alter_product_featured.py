# Generated by Django 4.2.4 on 2023-09-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.IntegerField(default=0),
        ),
    ]