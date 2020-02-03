from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    description = models.TextField(null=True,blank=True)
    price = models.IntegerField(default=100)
    image = models.ImageField(upload_to='upload_products',max_length=255,null=True,blank=True,default='static/images/shop/product9.jpg')
    #image = models.FileField(upload_to='static/images/products', verbose_name='My Photo',default='static/images/shop/product9.jpg')
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #requested_shipping = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.title)
    class Meta:
        unique_together = ('title','slug')
    def get_price(self):
        return self.price

#class ProductImage(models.Model):
#    product = models.ForeignKey(Product,on_delete=models.CASCADE,)
#    image = models.ImageField(upload_to='static/images/product/')
 #   featured = models.BooleanField(default=False)
 #   thumbnail = models.BooleanField(default=False)
 #   active = models.BooleanField(default=True)
 #   updated = models.DateTimeField(auto_now_add=False, auto_now=True)

 #   def __unicode__(self):
  #      return self.product.title
