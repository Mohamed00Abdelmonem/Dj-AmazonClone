from django.shortcuts import render
from product.models import Product, Brand, Review
from django.db.models import Count
from django.views.decorators.cache import cache_page

# Create your views here.


@cache_page(60 * 60 * 24)
def home(request):
    brands = Brand.objects.all().annotate(brand_count=Count('product_brand'))
    sale_products = Product.objects.filter(flag='sale')[:10] 
    new_products = Product.objects.filter(flag='new')[:6] 
    feature_products = Product.objects.filter(flag='feature')[:5]
    reviwes = Review.objects.all()[:10] 


    return render(request, 'settings/home.html',{
                                                'brands':brands , 
                                                'sale_products':sale_products, 
                                                'new_products':new_products, 
                                                'feature_products':feature_products, 
                                                'reviews':reviwes
                                                 })