from django.db import models

# Create your models here.

FLAG_TYPES = (
    ('Sale', 'Sale'),
    ('New', 'New'),
    ('Feature', 'Feature'),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'products')
    price = models.FloatField()
    flag = models.CharField(max_length=10, choices=FLAG_TYPES)
    sku = models.CharField(max_length=12)
    subtitle = models.CharField(max_length=300)
    description = models.TextField(max_length=40000)
    quantity = models.IntegerField()
    brand = models.ForeignKey('Brand', related_name='product_brand', on_delete=models.SET_NULL, null=True)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='product_image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')



        
