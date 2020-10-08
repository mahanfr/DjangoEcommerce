from django.contrib import admin
from products.models import (Product,
    Comment,
    ImageModel,
    Category,
    MasterCategory,)
#    Sku,)

# Register your models here.
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(ImageModel)
admin.site.register(Category)
admin.site.register(MasterCategory)
# admin.site.register(Sku)