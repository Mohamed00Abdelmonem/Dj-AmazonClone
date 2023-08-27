from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager

# Create your models here.

FLAG_TYPES = (
    ('sale', 'sale'),
    ('new', 'new'),
    ('feature', 'feature'),
)

class Product(models.Model):
    name = models.CharField(_("Name"),max_length=100)
    image = models.ImageField(_("Image"),upload_to= 'products')
    price = models.FloatField(_("Price"),)
    rate = models.IntegerField(_("Rate"),) 
    flag = models.CharField(_("Flag"),max_length=10, choices=FLAG_TYPES)
    sku = models.CharField(_("Sku"),max_length=12)
    tags = TaggableManager()
    subtitle = models.CharField(_("Subtitle"),max_length=300)
    description = models.TextField(_("Description"),max_length=40000)
    quantity = models.IntegerField(_("Quantity"),)
    brand = models.ForeignKey('Brand', verbose_name=_("Brand"), related_name='product_brand', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name  


class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"),related_name='product_image', on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='product_images')


    def __str__(self) -> str:
        return str(self.product)  


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    image = models.ImageField(_("Image"), upload_to='brands')


    def __str__(self) -> str:
        return self.name   


class Review(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.SET_NULL, null=True, related_name='review_auther')  
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='review_product', on_delete=models.CASCADE)
    rate = models.IntegerField(_("Rate"),) 
    review = models.CharField(_("Review"),max_length=300)
    created_at = models.DateTimeField(_("created at"),default=timezone.now)      


    def __str__(self) -> str:
        return f"{self.user} - {self.review }"  
