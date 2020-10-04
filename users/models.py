from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    # Inistial shipping with this fields
    address = models.TextField(blank=True,null=True)
    provice = models.CharField(max_length=150,null=True,blank=True)
    city = models.CharField(max_length=150,null=True,blank=True)
    town = models.CharField(max_length=100,null=True,blank=True)
    postCode = models.CharField(max_length=50,null=True,blank=True)
    telephone = models.CharField(max_length=50,null=True,blank=True)
    # credantial data to collect
    phonenumber = models.CharField(max_length=11,null=True)
    cardNumber = models.CharField(max_length=50,null=True)
    # additional info
    score = models.IntegerField(default=0,null=True)
    used_promocodes = models.ManyToManyField('checkout.Promocode')

    def __str__(self):
        return f'{self.user.username} Profile'
