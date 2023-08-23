from django.contrib import admin
from .models import Product, ProductImages, Brand, Review
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)