# Generated by Django 4.2.4 on 2024-03-15 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_max_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='max_quantity',
        ),
    ]
