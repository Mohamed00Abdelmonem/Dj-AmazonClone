from django.shortcuts import render
from product.models import Product, Brand, Review
from django.db.models import Count
from django.views.decorators.cache import cache_page

# Create your views here.


# @cache_page(60 * 3) # 3 minutes                                                                                                                                                                           
def home(request):
       brands = Brand.objects.all().annotate(brand_count=Count('product_brand'))
       sale_products = Product.objects.filter(flag='sale')[:1] 
       new_products = Product.objects.filter(flag='new')[:1] 
       feature_products = Product.objects.filter(flag='feature')[:1]
       reviwes = Review.objects.all()[:1] 

    #    print("brands:", brands)
    #    print("sale_products:", sale_products)
    #    print("new_products:", new_products)
    #    print("feature_products:", feature_products)
    #    print("reviwes:", reviwes)

       return render(request, 'settings/home.html', {
           'brands': brands,
           'sale_products': sale_products,
           'new_products': new_products,
           'feature_products': feature_products,
           'reviews': reviwes
       })
