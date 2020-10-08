from django.db import models
from django.conf import settings
from products.models import Product

class OrderProducts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    orderd = models.BooleanField(default=False)
 
    def getTotalPrice(self):
        return self.product.price * self.quantity

    def getDiscountPrice(self):
        return self.product.getOffedPrice() * self.quantity

    def __str__(self):
        return str(self.product.title) + '  ' + str(self.quantity)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderProducts)
    start_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()
    orderd = models.BooleanField(default=False)
    shippingAddress = models.ForeignKey('checkout.ShippingAddress',on_delete=models.SET_NULL,blank=True,null=True)
    promo_discount = models.ForeignKey('checkout.PromoCode',on_delete=models.SET_NULL,blank=True,null=True)
    refund_discripton = models.TextField(null=True,blank=True)
    checkout_failed = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    
    def getTotalPrice(self):
        price = 0
        for item in self.items.all():
            price += item.getTotalPrice()
        return price

    def getSumQuantity(self):
        quantity = 0
        for item in self.items.all():
            quantity += item.quantity
        return quantity

    def getFinalPrice(self):
        price = 0
        for item in self.items.all():
            price += item.getDiscountPrice()
        return price

    def getPayablePrice(self):
        finalPrice = self.getFinalPrice()
        if(self.promo_discount):
            return finalPrice - ((finalPrice * self.promo_discount.promo_discount) / 100)
        return finalPrice

    def getTotalDiscount(self):
        return self.getTotalPrice() - self.getFinalPrice()

    def __str__(self):
        return '# '+str(self.id)
