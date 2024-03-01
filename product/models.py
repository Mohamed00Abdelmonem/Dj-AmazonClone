from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.db.models.aggregates import Avg
from django.utils.html import format_html


# Create your models here.

FLAG_TYPES = (
    ('sale', 'sale'),
    ('new', 'new'),
    ('feature', 'feature'),
)

# __________________________________________________________________________________

class Product(models.Model):
    name = models.CharField(verbose_name=_('Name'),max_length=100)
    image = models.ImageField(_("Image"),upload_to= 'products')
    price = models.FloatField(_("Price"),)
    rate = models.IntegerField(_("Rate"),) 
    flag = models.CharField(_("Flag"),max_length=10, choices=FLAG_TYPES)
    sku = models.CharField(_("Sku"),max_length=12)
    tags = TaggableManager()
    subtitle = models.CharField(_("Subtitle"),max_length=300)
    description = models.TextField(_("Description"),max_length=40000)
    quantity = models.IntegerField(_("Quantity"),)
    max_quantity = models.IntegerField(_("Max Quantity"), default=100)  # Change '100' to your desired default value

    brand = models.ForeignKey('Brand', verbose_name=_("Brand"), related_name='product_brand', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def quantity_progress_bar(self):
        if self.quantity is not None:
            percentage = round((self.quantity / self.max_quantity * 100), 2)
        else:
            percentage = 0

        return format_html(
            '<progress value="{}" max="100"></progress><span style="font-weight:bold">{:.2f}%</span>',
            percentage,
            percentage
        )
    

    # instance method = each object , self = object
    def avg_rate(self):
        avg = self.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs) 
# __________________________________________________________________________________

class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"),related_name='product_image', on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='product_images')


    def __str__(self) -> str:
        return str(self.product)  

# __________________________________________________________________________________


class Brand(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    image = models.ImageField(_("Image"), upload_to='brands')
    slug = models.SlugField(null=True, blank=True)


    def __str__(self) -> str:
        return self.name   
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

# __________________________________________________________________________________


class Review(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.SET_NULL, null=True, related_name='review_auther')  
    product = models.ForeignKey(Product, verbose_name=_("Product"), related_name='review_product', on_delete=models.CASCADE)
    rate = models.IntegerField(_("Rate"),) 
    review = models.CharField(_("Review"),max_length=300)
    created_at = models.DateTimeField(_("created at"),default=timezone.now)      


    def __str__(self) -> str:
        return f"{self.user} - {self.review }"  


# __________________________________________________________________________________
