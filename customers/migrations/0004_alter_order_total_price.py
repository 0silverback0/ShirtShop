# Generated by Django 4.2.4 on 2023-08-27 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
