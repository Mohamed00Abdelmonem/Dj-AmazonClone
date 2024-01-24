
from modeltranslation.translator import translator, TranslationOptions
from .models import Product, Review

# for Person model
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'flag', 'subtitle', 'description')

translator.register(Product, ProductTranslationOptions)


class ReviewTranslationOptions(TranslationOptions):
    fields = ('review',)

translator.register(Review, ReviewTranslationOptions)