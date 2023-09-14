from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductListSerializer,ProductDetailSerializer, BrandListSerializer, BrandDetailSerializer
from .models import Product, Brand
from rest_framework import generics

# ______________________________________________________________________


# Function 

# @api_view(['GET']) # HTTP method
# def product_list_api(request):
#     products = Product.objects.all()[:20]   # return list
#     data = ProductListSerializer(products, many=True, context={'request':request}).data # conver to json
#     return Response({'product':data})


# @api_view(['GET']) # HTTP method
# def product_detail_api(request, product_id):
#     products = Product.objects.get(id=product_id)   # return list
#     data = ProductDetailSerializer(products, context={'request':request}).data # conver to json
#     return Response({'product':data})



# class based view generics
class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer



class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer    



class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()  
    serializer_class = BrandListSerializer 


class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer    

