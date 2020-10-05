from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseForbidden
from cart.models import Order

class Management_index(View):
    def get(self,*args,**kwargs):
        if self.request.user.is_superuser:
            context = {
                'orders': Order
            }
            return render(self.request,'management/index.html')
        else:
            return HttpResponseForbidden()
