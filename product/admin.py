from django.contrib import admin
from .models import Product, ProductImages, Brand, Review
# Register your models here.

class ProductImagesTabular(admin.TabularInline):
    model = ProductImages



class ProductAdim(admin.ModelAdmin):
    list_display = ['name', 'flag', 'price', 'quantity', 'brand']
    list_filter = ['flag', 'brand']
    search_fields = ['name', 'subtitle', 'description'] 
    inlines = [ProductImagesTabular]



admin.site.register(Product, ProductAdim)
admin.site.register(ProductImages)
admin.site.register(Brand)
admin.site.register(Review)