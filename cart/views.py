from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render , get_object_or_404 , redirect
from .models import OrderProducts , Order
from products.models import Product
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views.generic import DetailView ,View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def add_to_cart(request,product_id):
    item = get_object_or_404(Product,id=product_id)
    order_item,created = OrderProducts.objects.get_or_create(
        product=item,
        user=request.user,
        orderd = False)
    order_qs = Order.objects.filter(user=request.user,orderd=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product__id=item.id).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request,'item quantity was updated')
        else:
            messages.info(request,'item added to your shoping cart')
            order.items.add(order_item)
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user,order_date=order_date)
        order.items.add(order_item)
        messages.info(request,'item added to your shoping cart')
    
    return redirect('order-summary')

@login_required
def remove_from_cart(request,product_id):
    item = get_object_or_404(Product,id=product_id)
    order_qs = Order.objects.filter(user=request.user,orderd=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product__id=item.id).exists():
            order_item = OrderProducts.objects.filter(product=item,user=request.user,orderd = False)[0]
            messages.info(request,'your item removed properly')
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
        else:
            # item dose not exists
            messages.info(request,'item dose not exsist')
            # return redirect('product',product_id=product_id)
            return redirect('order-summary')
    else:
        # order dose not exist
        messages.info(request,'your cart is empty')
        return redirect('order-summary')
        # return redirect('product',product_id=product_id)
    return redirect('order-summary')
    #return redirect('product',product_id=product_id)

@login_required
def Delete_product_from_cart(request,product_id):
    item = get_object_or_404(Product,id=product_id)
    order_qs = Order.objects.filter(user=request.user,orderd=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(product__id=item.id).exists():
            order_item = OrderProducts.objects.filter(product=item,user=request.user,orderd = False)[0]
            messages.info(request,'your item Deleted')
            order_item.delete()
        else:
            # item dose not exists
            messages.info(request,'item dose not exsist')
            # return redirect('product',product_id=product_id)
            return redirect('order-summary')
    else:
        # order dose not exist
        messages.info(request,'your cart is empty')
        return redirect('order-summary')
        # return redirect('product',product_id=product_id)
    return redirect('order-summary')
    #return redirect('product',product_id=product_id)

class AddToCart(LoginRequiredMixin,View):
    def post(self,*args,**kwargs):
        pass


class OrderSummaryView(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        try:
            order = Order.objects.get(user=self.request.user,orderd=False)
            context = {
                'object':order,
            }
            return render(self.request,'cart/order_summary.html',context=context)
        except ObjectDoesNotExist:
            return redirect('index')
