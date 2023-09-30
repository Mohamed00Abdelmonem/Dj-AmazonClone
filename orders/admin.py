from django.contrib import admin
from .models import Cart, CartDetail, Order, OrderDetail, Coupon
# Register your models here.


admin.site.register(Cart)
admin.site.register(CartDetail)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Coupon)