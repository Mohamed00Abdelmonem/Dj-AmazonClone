from django.contrib import admin
from .models import Product, Brand, Review, ProductImages, Add_To_Favourite
from modeltranslation.admin import TranslationAdmin


class ProductImagesTabular(admin.TabularInline):
    model = ProductImages

class ProductAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'flag', 'price', 'quantity', 'brand', 'quantity_progress_bar']
    list_filter = ['flag', 'brand']
    search_fields = ['name']
    inlines = [ProductImagesTabular]
    ordering = ('-id',) 

  




admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImages)
admin.site.register(Add_To_Favourite)
