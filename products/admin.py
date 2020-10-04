from django.contrib import admin
from products.models import Product ,Comment ,ImageModel ,Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(ImageModel)
admin.site.register(Category)