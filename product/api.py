from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

# Function 
@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()[:20]   # return list
    data = ProductSerializer(products, many=True, context={'request':request}).data # conver to json
    return Response({'product':data})


@api_view(['GET'])
def product_detail_api(request, product_id):
    products = Product.objects.get(id=product_id)   # return list
    data = ProductSerializer(products, context={'request':request}).data # conver to json
    return Response({'product':data})

