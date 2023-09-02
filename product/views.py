from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Brand, Review
# Create your views here.


class ProductList(ListView):
    model= Product

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


class BrandList(ListView):
    model = Brand # context : object_list , model_list





class BrandDetail(ListView):
    model = Product
    template_name = 'product/brand_detail.html'


# كدا ف الداله دي بيقولك هات كل المنتجات اللي البراند بتاعهها هو اللي انا واقف عليه دلوقتي
    def get_queryset(self):
        brand = Brand.objects.get(slug=self.kwargs['slug'])
        return super().get_queryset().filter(brand = brand)


# دا بيجيب تفاصيل الراند بتاعي دلوقتي زي الصوره و الاسم و كدا 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    




# نفس الكود بس باستخدام ال  function based view
# def BrandDetail(request, slug):
#     data = Brand.objects.get(slug=slug)
#     brand = Product.objects.filter(brand=data)
#     return render(request, 'product/brand_detail.html', {'brands':brand, 'data':data})
