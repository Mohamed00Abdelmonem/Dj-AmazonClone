from rest_framework import serializers
from .models import Product, Brand


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 



class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'         



class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='product_brand', many=True)
    class Meta:
        model = Brand
        fields = '__all__'                 