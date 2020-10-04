from django.db import models
from django.conf import settings

# Create your models here.
class ShippingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    address = models.TextField(blank=True,null=True)
    provice = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    postCode = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50,blank=True)

    def __str__(self): 
        return self.user.username

class PromoCode(models.Model):
    code = models.CharField(max_length=15)
    expirationDate = models.DateTimeField()
    min_price = models.BigIntegerField()
    promo_discount = models.IntegerField()

    def __str__(self):
        return self.code
    