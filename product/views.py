from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Product, Brand, Review
from django.db.models.aggregates import Count
from accounts.models import Profile
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .tasks import send_emails

from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.

# __________________________________________________________________________________


@cache_page(60 * 60 * 1)
def debug(request):
    data = Product.objects.all()
    user_data = Profile.objects.get(user=request.user)
    
    send_emails.delay()      
    return render(request, 'product/debug.html', {"data":data, 'user_data':user_data})




# __________________________________________________________________________________
# @method_decorator(cache_page(60 * 60 * 5), name='dispatch')

class ProductList(ListView):
    model= Product
    paginate_by =30

    def get_queryset(self) -> QuerySet[Any]:
        # Order products by ID in descending order
        return Product.objects.all().order_by('-id')

# __________________________________________________________________________________


class ProductDetail(DetailView):
    model= Product   


    def get_context_data(self, **kwargs): 
        context =  super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["related_products"] = Product.objects.filter(brand=self.get_object().brand)
        return context
    
# what's meaning the function or this context 
# 1 - line 17 meaning make override for this class 
# 2 - line 18 meaning reviews in key and value this Review.objects.filter(product=self.get_object())
# 3 - line 19 another context name key = related_products , vlaue = that  Product.objects.filter(brand=self.get_object().brand)

# __________________________________________________________________________________
# @method_decorator(cache_page(60 * 60 * 5), name='dispatch')
class BrandList(ListView):
    model = Brand # context : object_list , model_list
    queryset = Brand.objects.annotate(product_count=Count('product_brand'))
    paginate_by = 20

# __________________________________________________________________________________

class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'
    paginate_by = 20

# كدا ف الداله دي بيقولك هات كل المنتجات اللي البراند بتاعهها هو اللي انا واقف عليه دلوقتي
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand = brand)
    
 
# دا بيجيب تفاصيل البراند بتاعي دلوقتي زي الصوره و الاسم و كدا 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        # دا كود ممكن من خلاله نستغنا عن داله الاسعلام اللي فوق دي 
        # context["object_list"] = Product.objects.filter(brand=context['brand'])
        return context
    

# نفس الكود بس باستخدام ال  function based view
# def BrandDetail(request, slug):
#     data = Brand.objects.get(slug=slug)
#     brand = Product.objects.filter(brand=data)
#     return render(request, 'product/brand_detail.html', {'brands':brand, 'data':data})


# __________________________________________________________________________________

def add_review(request, slug):
    product = Product.objects.get(slug=slug)
    rate = request.POST['rate']
    review = request.POST['review']

    Review.objects.create(
        product = product,
        rate = rate,
        review = review,
        user = request.user
    )

    # new reviews
    reviews = Review.objects.filter(product=product)
    html = render_to_string('include/reviews_include.html', {'reviews':reviews})
    return JsonResponse({'result':html})

    # return redirect(f'/products/product/{product.slug}')