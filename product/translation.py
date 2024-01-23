
from modeltranslation.translator import translator, TranslationOptions
from .models import Product

# for Person model
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'flag', 'price', 'subtitle', 'description', 'quantity', 'brand')

translator.register(Product, ProductTranslationOptions)