from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Order, OrderDetail, Cart, CartDetail, Coupon
from product.models import Product
from settings.models import DeliveryFee
from django.shortcuts import get_object_or_404
import datetime
from django.http import JsonResponse
from django.template.loader import render_to_string
from utils.generate_code import generate_code
from django.conf import settings
import stripe







# _________________________________________________________________________________

class OrderList(LoginRequiredMixin,ListView):
    model = Order
    paginate_by = 10 

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset
    

    
# _________________________________________________________________________________



def add_to_cart(request):
    quantity = request.POST['quantity']
    product = Product.objects.get(id=request.POST['product_id'])

    cart = Cart.objects.get(user=request.user, status='InProgress')
    cart_detail, created = CartDetail.objects.get_or_create(cart=cart, product=product) 


    cart_detail.quantity = int(quantity)
    cart_detail.total = round(int(quantity)* product.price,2)
    cart_detail.save()
    return redirect(f'/products/product/{product.slug}')

# _________________________________________________________________________________


def remove_from_cart(request, id):
    cart_detail = CartDetail.objects.get(id=id)
    cart_detail.delete()
    return redirect('/products/')

# _________________________________________________________________________________


 

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user, status='InProgress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee
    pub_key = settings.STRIPE_API_KEY_PUBLISHABLE


    if request.method == 'POST':
        coupon = get_object_or_404(Coupon, code=request.POST['coupon_code']) #  return 404
        # coupon = Coupon.objects.get(code=request.data['coupon_code']) # return Error

        if coupon and coupon.quantity > 0 :
            today_date = datetime.datetime.today().date()

            if today_date >= coupon.start_date.date() and today_date <= coupon.end_date.date():
            # if today_date >= coupon_start_date and today_date <= coupon_end_date:
                coupon_value  = cart.cart_total() * coupon.discount/100
                cart_total = cart.cart_total() - coupon_value

                coupon.quantity -= 1
                coupon.save()

                cart.coupon = coupon
                cart.total_after_coupon = cart_total
                cart.save()

                total = delivery_fee + cart_total

                cart = Cart.objects.get(user=request.user, status='InProgress')

                # return render(request, 'orders/checkout.html',
                #               {'cart_detail':cart_detail,
                #                'sub_total':cart_total,
                #                'cart_total': total,
                #                'delivery_fee': total,
                #                'coupon_value':coupon_value,

                #               }) 
                                  

                html = render_to_string('include/checkout_table.html', {'cart_detail':cart_detail,
                                        'sub_total':cart_total,
                                        'cart_total': total,
                                        'delivery_fee': total,
                                        'coupon_value':coupon_value,
                                        'pub_key': pub_key,

                                        })
                return JsonResponse({'result':html})


    return render(request, 'orders/checkout.html', 
                   {'cart_detail':cart_detail,
                    'sub_total':cart.cart_total(),
                    'cart_total': cart.cart_total() + delivery_fee,
                    'delivery_fee': delivery_fee,
                    'coupon_value':0,
                    'pub_key': pub_key
                   })    

            
   

# _________________________________________________________________________________


def process_payment(request):
    cart = Cart.objects.get(user=request.user, status='InProgress')
    cart_detail = CartDetail.objects.filter(cart=cart)
    delivery_fee = DeliveryFee.objects.last().fee

    if cart.total_after_coupon:
        total = cart.total_after_coupon + delivery_fee

    else:
        total = cart.cart_total() + delivery_fee

    code = generate_code()
    
    stripe.api_key = settings.STRIPE_API_KEY_SECRET

    items = [{
        'price_data': {
            'currency': 'usd',
            'product_data': {
            'name': code ,
            },
            'unit_amount': int(total*100),
            },
        'quantity': 1,
    }]


    checkout_session = stripe.checkout.Session.create(  
            line_items=items,
            mode='payment',
            success_url="https://dj-amazonclone.onrender.com/orders/checkout/payment/success",
            cancel_url="https://dj-amazonclone.onrender.com/orders/checkout/payment/failed",
        )
    return JsonResponse({'session':checkout_session})





# _________________________________________________________________________________

def payment_success(request):
    cart = Cart.objects.get(user=request.user, status='InProgress')
    cart_detail = CartDetail.objects.filter(cart=cart)

    new_order = Order.objects.create(
        user = request.user,
        coupon = cart.coupon,
        total_after_coupon = cart.total_after_coupon
    )

      # cart_detail --> order_detail --> loop
    for object in cart_detail:
            OrderDetail.objects.create(
                order = new_order,
                product = object.product,
                quantity = object.quantity,
                price = object.product.price,
                total = round(int(object.quantity) * object.product.price,2)

            )
    cart.status = 'Completed'  
    cart.save()

    # send email


    return render(request, 'orders/success.html', {})
# _________________________________________________________________________________

def payment_failed(request):
    return render(request, 'orders/failed.html', {})



# _________________________________________________________________________________
