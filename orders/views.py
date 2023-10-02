from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Order
# Create your views here.



class OrderList(ListView):
    model = Order
    paginate_by = 10 

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        return queryset