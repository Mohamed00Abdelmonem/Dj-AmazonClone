from .serializers import ProductListSerializer,ProductDetailSerializer, BrandListSerializer, BrandDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['flag', 'brand']
    search_fields = ['name', 'subtitle', 'description']


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer    



class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()  
    serializer_class = BrandListSerializer 


class BrandDetailApi(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer    

