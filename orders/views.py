from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Order, Cart, CartDetail, Coupon
# Create your views here.



class OrderList(LoginRequiredMixin,ListView):
    model = Order
    paginate_by = 10 

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset
    

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user, status='InProgress')
    cart_detail = CartDetail.objects.filter(cart=cart)

    return render(request, 'orders/checkout.html', {'cart_detail':cart_detail})    