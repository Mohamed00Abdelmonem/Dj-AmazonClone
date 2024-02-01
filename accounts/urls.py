from django.urls import path
from .views import signup, activate, dashboard, profile, EditProfile

app_name = 'accounts'

urlpatterns= [
    path('signup', signup, name='signup'),
    path('<str:username>/activate', activate),
    path('profile', profile, name='profile_user'),
    path('dashboard', dashboard),
    path('edit-profile/', EditProfile.as_view(), name='edit_profile'),

]


