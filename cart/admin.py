from django.contrib import admin
from .models import Order,OrderProducts

admin.site.register(Order)
admin.site.register(OrderProducts)
