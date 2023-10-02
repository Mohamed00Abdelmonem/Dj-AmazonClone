from django.urls import path
from .views import OrderList, checkout


urlpatterns = [
    path('', OrderList.as_view()),
    path('checkout', checkout)

]