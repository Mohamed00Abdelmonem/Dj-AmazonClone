from django.urls import path
from .views import signup, activate, dashboard

app_name = 'accounts'

urlpatterns= [
    path('signup', signup, name='signup'),
    path('<str:username>/activate', activate),
    path('dashboard', dashboard),
]