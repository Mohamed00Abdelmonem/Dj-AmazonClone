from django.urls import path
from .views import OrderList, checkout, add_to_cart, remove_from_cart, process_payment, payment_success, payment_failed
from .api import CartDetailCreateAPI, OrderListAPI, OrderDetailAPI, CreateOrderAPI, ApplayCouponAPI




app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view()),
    path('checkout', checkout, name='checkout'),
    path('checkout/payment', process_payment),
    path('checkout/payment/success', payment_success),
    path('checkout/payment/failed', payment_failed),
    path('add-to-cart', add_to_cart, name='add_to_cart'),
    path('<int:id>/remove-form-cart', remove_from_cart),



    # API
    path('api/list/<str:username>', OrderListAPI.as_view()),
    path('api/list/<str:username>/create-order', CreateOrderAPI.as_view()),
    path('api/list/<str:username>/<int:pk>', OrderDetailAPI.as_view()),
    path('api/<str:username>/cart', CartDetailCreateAPI.as_view()),
    path('api/<str:username>/cart/applay-coupon', ApplayCouponAPI.as_view()),

]