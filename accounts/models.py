from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile')
    code = models.CharField(max_length=10, default=generate_code)





ADRESS_TYPE = (
    ('Home','Home' ),
    ('Bussiness', 'Bussiness'),
    ('Academy','Academy' ),
    ('Office','Office' ),
    ('Others','Others' ),
)


class Address(models.Model):
    user = models.ForeignKey(User, related_name='user_address', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=ADRESS_TYPE)
    address = models.TextField(max_length=300)
    notes = models.TextField(max_length=400, null=True, blank=True)






PHONE_TYPE = (
    ('Primary','Primary' ),
    ('Secondry', 'Secondry'),
    ('Academy','Academy' ),
    ('Office','Office' ),
    ('Others','Others' ),
)


class Phone(models.Model):
    user = models.ForeignKey(User, related_name='user_phone', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=PHONE_TYPE)
    phone = models.CharField(max_length=25)
