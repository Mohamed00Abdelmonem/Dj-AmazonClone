from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail, debug
from .api import  ProductListApi, ProductDetailApi, BrandListApi, BrandDetailApi



urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('brands/', BrandList.as_view()),
    path('brands/<slug:slug>/', BrandDetail.as_view()),
    path('debug/', debug),

    # api urls
    path('api/list/', ProductListApi.as_view()),
    path('api/list/<int:pk>', ProductDetailApi.as_view()),

    path('brand/api/list/', BrandListApi.as_view()),
    path('brand/api/list/<int:pk>', BrandDetailApi.as_view()),

]
    