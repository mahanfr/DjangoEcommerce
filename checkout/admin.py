from django.contrib import admin
from .models import ShippingAddress , PromoCode

# Register your models here.
admin.site.register(ShippingAddress)
admin.site.register(PromoCode)