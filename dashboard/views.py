from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from cart.models import Order

class Dashboard(View):
    def get(self,*args,**kwargs):
        order_qs = Order.objects.filter(user=self.request.user,orderd=True)
        context = {
            'orders':order_qs,
        }
        return render(self.request,'dashboard/index.html',context=context)