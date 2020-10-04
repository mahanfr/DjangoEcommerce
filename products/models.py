from django.db import models
from django.conf import settings

class Product(models.Model):
    title = models.CharField(max_length=100)
    categories = models.ForeignKey('products.Category',on_delete=models.SET_NULL,null=True)
    discription = models.TextField()
    details = models.TextField()
    features = models.TextField()
    price = models.BigIntegerField()
    discount = models.IntegerField()
    quantity = models.BigIntegerField()
    review_score = models.BigIntegerField(default=0)
    review_count = models.BigIntegerField(default=0)
    images = models.ManyToManyField('products.Imagemodel')
    comments = models.ManyToManyField('products.Comment',blank=True)

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