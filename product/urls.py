from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail, debug, add_review, add_to_favourite, show_favourites
from .api import  ProductListApi, ProductDetailApi, BrandListApi, BrandDetailApi

app_name = 'product'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('brands/', BrandList.as_view()),
    path('brands/<slug:slug>/', BrandDetail.as_view()),
    path('debug/', debug),
    path('<slug:slug>/add-review', add_review, name='add_review'),
    path('add_to_favourite', add_to_favourite, name='add_to_favourite'),
    path('favourites', show_favourites, name='show_favourites'),

    # api urls
    path('api/list/', ProductListApi.as_view()),
    path('api/list/<int:pk>', ProductDetailApi.as_view()),

    path('brand/api/list/', BrandListApi.as_view()),
    path('brand/api/list/<int:pk>', BrandDetailApi.as_view()),

]
    