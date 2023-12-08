from django.contrib import admin
from .models import Profile, Phone, Address
# Register your models here.

admin.site.register(Profile)
admin.site.register(Phone)
admin.site.register(Address)