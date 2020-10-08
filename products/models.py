from django.db import models
from django.conf import settings

class Product(models.Model):
    title = models.CharField(max_length=100)
    categories = models.ForeignKey('products.Category',on_delete=models.SET_NULL,null=True)
    discription = models.TextField()
    details = models.TextField()
    features = models.TextField()
    price = models.BigIntegerField(default=1000)
    discount = models.IntegerField(default=0)
    quantity = models.BigIntegerField(default=1)
    review_count = models.BigIntegerField(default=0)
    images = models.ManyToManyField('products.Imagemodel')

    # def getLowestPrice(self):
    #     qs = self.sku_set.all().values('price')
    #     priceList = [d['price'] for d in qs if 'price' in d]
    #     self.lowestPrice = min(priceList)
    #     return min(priceList)

    # def getLowestPriceDiscount(self):
    #     price = self.getLowestPrice()
    #     qs = (self.sku_set.all().filter(price=price).values('discount'))
    #     if qs:
    #         return qs[0]['discount']
    #     else:
    #         return 0

    def getOffedPrice(self):
        return self.price - ((self.price * self.discount)/100)

    def getMainImage(self):
        for image in self.images.all():
            if image.is_main:
                return image
        return self.images.all()[0]

    def getFeaturesList(self):
        return str(self.features).split('#')

    def __str__(self):
        return 'Product #' + str(self.id)


class ImageModel(models.Model):
    image = models.ImageField(default='default.jpg',upload_to='product_photos')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return 'image ' + str(self.id)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    discription = models.TextField()
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return 'comment of ' + str(self.user.username)

class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class MasterCategory(models.Model):
    title = models.CharField(max_length=100)
    comments = models.ManyToManyField('products.Category',blank=True)
    def __str__(self):
        return self.title

# class Sku(models.Model):
#     item = models.ForeignKey('products.Product',on_delete=models.CASCADE)
#     price = models.BigIntegerField(default=1000)
#     discount = models.IntegerField(default=0)
#     quantity = models.BigIntegerField(default=1)
#     # Veraitery
#     # Modify for later use
#     color = models.CharField(max_length=20,blank=True,null=True)
#     size = models.CharField(max_length=20,blank=True,null=True)
#     model = models.CharField(max_length=20,blank=True,null=True)
#     additionalVer = models.CharField(max_length=20,blank=True,null=True)
#     additionalVer2 = models.CharField(max_length=20,blank=True,null=True)

#     def getOffedPrice(self):
#         return self.price - ((self.price * self.discount)/100)

#     def __str__(self):
#         return f'({self.item.title})({self.color})({self.size})({self.model})'