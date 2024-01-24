from django.contrib import admin
from .models import Product, Brand, Review, ProductImages
from modeltranslation.admin import TranslationAdmin

# Register your models here.



class ProductImagesTaburlar(admin.TabularInline):
    model = ProductImages


class ProductAdmin(TranslationAdmin):
    list_display = ['name', 'flag', 'price', 'quantity', 'brand']
    list_filter = ['flag', 'brand']
    search_fields = ['name']
    inlines = [ProductImagesTaburlar]





admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImages)