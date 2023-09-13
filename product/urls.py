from django.urls import path
from .views import ProductList, ProductDetail, BrandList, BrandDetail, debug
from .api import product_list_api, product_detail_api



urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('brands/', BrandList.as_view()),
    path('brands/<slug:slug>/', BrandDetail.as_view()),
    path('debug/', debug),

    # api urls
    path('api/list/', product_list_api),
    path('api/list/<int:product_id>', product_detail_api),

]
    