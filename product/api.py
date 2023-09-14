from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, BrandSerializer
from .models import Product, Brand
from rest_framework import generics

# ______________________________________________________________________


# Function 
@api_view(['GET']) # HTTP method
def product_list_api(request):
    products = Product.objects.all()[:20]   # return list
    data = ProductSerializer(products, many=True, context={'request':request}).data # conver to json
    return Response({'product':data})


@api_view(['GET']) # HTTP method
def product_detail_api(request, product_id):
    products = Product.objects.get(id=product_id)   # return list
    data = ProductSerializer(products, context={'request':request}).data # conver to json
    return Response({'product':data})



# class based view generics
class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    



class BrandListApi(generics.ListAPIView):
    queryset = Brand.objects.all()  
    serializer_class = BrandSerializer 


class BrandDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = BrandSerializer    

