from rest_framework import serializers
from .models import Cart, CartDetail, Order, OrderDetail
from product.serializers import ProductListSerializer


class CartDetailSerializer(serializers.ModelSerializer):
    # product = ProductListSerializer() ------- = show all detail from product 
    product = serializers.StringRelatedField() # ------ show product name only
    class Meta:
        model = CartDetail
        fields = '__all__'




class CartSerializer(serializers.ModelSerializer):
    cart_detail = CartDetailSerializer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'
