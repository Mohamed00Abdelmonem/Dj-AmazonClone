from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.generate_code import generate_code

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile', null=True,blank=True)
    code = models.CharField(max_length=10, default=generate_code)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )



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
