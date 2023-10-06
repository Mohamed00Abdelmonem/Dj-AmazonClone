from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from utils.generate_code import generate_code
from product.models import Product





CART_STATUS = {
    ('InProgress','InProgress'),
    ('Completed','Completed'),
}

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart_user', on_delete=models.SET_NULL,null=True, blank=True)
    status = models.CharField(max_length=10, choices=CART_STATUS)

    def __str__(self):
        if self.user:
            return f"Cart for {self.user.username}"
        else:
            return f"Cart (No User)"

    def cart_total(self):
        total = 0 
        for item in self.cart_detail.all():
            total += item.total
        return round(total,2)

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(null=True, blank=True)

 
    def __str__(self):
        if self.cart:
            return f"cart_detail {self.cart}"
        else:
            return f"Cart (No User)"





ORDER_STATUS = {
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
}

class Order(models.Model):
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.SET_NULL,null=True, blank=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUS)
    code = models.CharField(max_length=9 ,default=generate_code())
    order_time = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(null=True, blank=True)
    coupon = models.ForeignKey('Coupon', related_name='order_coupon', on_delete=models.SET_NULL, null=True, blank=True)
    total_after_coupon = models.FloatField(null=True, blank=True )

    def __str__(self):
            return f'{self.user}'
       




class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_product', on_delete=models.SET_NULL, null=True, blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.FloatField(null=True, blank=True)

    def __str__(self):
            return f'{self.order}'






class Coupon(models.Model):
    code = models.CharField(max_length=20)
    discount = models.IntegerField()
    quantity= models.IntegerField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.code}'

    def save(self, *args, **kwargs):
      week = datetime.timedelta(days=7)
      self.end_date = self.start_date + week
      super (Coupon, self).save(*args, **kwargs)