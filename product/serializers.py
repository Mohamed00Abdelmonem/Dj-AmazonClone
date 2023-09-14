from rest_framework import serializers
from .models import Product, Brand
from django.db.models.aggregates import Avg


#__________________________________________________________________________





class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'         






#__________________________________________________________________________


class ProductListSerializer(serializers.ModelSerializer):
    # brand = BrandListSerializer() # this line code for return all detail for brand for this object or product 
    brand = serializers.StringRelatedField() # this line code for return str in model for this brand == name brand  
    avg_rate = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    # price_with_tax = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__' 

    # method for avrage rate for product
    def get_avg_rate(self, product):
        avg = product.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']

    def get_review_count(self,product:Product):
        reviews = product.review_product.all().count()
        return reviews
    
    # Method for Test only 

    # def get_price_with_tax(self, product):
    #     return product.price*1.5
    




#__________________________________________________________________________





class ProductDetailSerializer(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__' 

     # method for avrage rate for product

    def get_avg_rate(self, product):
        avg = product.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']

    def get_review_count(self,product:Product):
        reviews = product.review_product.all().count()
        return reviews




#__________________________________________________________________________









class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(source='product_brand', many=True)
    class Meta:
        model = Brand
        fields = '__all__'                 