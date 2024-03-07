from django.contrib import admin
from .models import Product, Brand, Review, ProductImages
from modeltranslation.admin import TranslationAdmin
from django.utils.html import format_html
from django.template.defaultfilters import floatformat

class ProductImagesTabular(admin.TabularInline):
    model = ProductImages

class ProductAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'flag', 'price', 'quantity', 'brand', 'quantity_progress_bar']
    list_filter = ['flag', 'brand']
    search_fields = ['name']
    inlines = [ProductImagesTabular]
    ordering = ('-id',) 

    fieldsets = (
        ('Product Details', {
            'fields': (
                'name', 'image', 'price', 'rate', 'flag', 'sku',
                'tags', 'subtitle', 'description', 'quantity', 'max_quantity', 'brand', 'slug',
                'quantity_progress_bar',
            )
        }),
    )

    readonly_fields = ('quantity_progress_bar',)

    def quantity_progress_bar(self, obj):
        if obj.quantity is not None:
            percentage = round((obj.quantity / obj.max_quantity * 100), 2)
        else:
            percentage = 0

        return format_html(
            '<progress value="{}" max="100"></progress><span style="font-weight:bold">{}</span>',
            percentage,
            floatformat(percentage, 2) + '%'
        )





admin.site.register(Product, ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)
admin.site.register(ProductImages)
