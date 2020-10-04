from django.shortcuts import render ,redirect
from django.views.generic import View
from cart.models import Order
from django.core.exceptions import ObjectDoesNotExist
from .models import ShippingAddress , PromoCode
from .forms import CheckoutForm ,PromoCodeForm
from django.http import HttpResponseForbidden
from django.contrib import messages

class CheckoutView(View):
    def get(self,*args,**kwargs):
        order = Order.objects.get(user=self.request.user,orderd=False)
        if(order):
            if(order.items.count()>0):
                form = CheckoutForm()
                form_promo = PromoCodeForm()
                context = {
                    'order_items' : order,
                    'form' : form,
                    'promo_form':form_promo,
                }
                return render(self.request,'checkout/checkout.html',context=context)
        return HttpResponseForbidden()

    def post(self,*args,**kwargs):
        order = Order.objects.get(user=self.request.user,orderd=False)
        if(order):
            if(order.items.count()>0):
                form = CheckoutForm(self.request.POST or None)
                if form.is_valid():
                    address_field = form.cleaned_data.get('addressfield')
                    provice = form.cleaned_data.get('provice')
                    city = form.cleaned_data.get('city')
                    town = form.cleaned_data.get('town')
                    postCode = form.cleaned_data.get('postCode')
                    telephone = form.cleaned_data.get('telephone')
                    save_info = form.cleaned_data.get('save_info')
                    shippingAddress = ShippingAddress(user=self.request.user,
                        address=address_field, provice=provice, city=city, town=town,
                        postCode=postCode, telephone=telephone)
                    shippingAddress.save()

                    if(save_info == True):
                        profile = self.request.user.profile
                        profile.address = address_field
                        profile.provice = provice
                        profile.city = city
                        profile.town = town
                        profile.postCode = postCode
                        profile.telephone = telephone
                        profile.save()


                    # Transfer to payment
                    order_items = order.items.all()
                    order_items.update(orderd=True)
                    for item in order_items:
                        item.save()

                    order.shippingAddress = shippingAddress
                    order.orderd = True
                    order.save()
                    #TODO :add redirect to payment methodes
                    return redirect('index')
                messages.warning(self.request,message='لطفا ورودی ها خود را کنترل کنید')
                return redirect('checkout')
        messages.warning(self.request,message='شما دسترسی لازم را ندارید')
        return redirect('index')

class SubmitPromoView(View):
    def post(self,*args,**kwargs):
        form = PromoCodeForm(self.request.POST or None)
        if form.is_valid():
            promoCode = form.cleaned_data.get('promoCode')
            try:
                promoCode = Promocode.objects.get(code=promoCode)
                Order.promo_discount = promoCode.promo_discount
                order = Order.objects.get(user=self.request.user,orderd=False)
                order.promo_discount = promoCode.promo_discount
                order.save()
                messages.success(self.request,'کد با موفقیت اعمال شد')
                return redirect('checkout')
            except ObjectDoesNotExist:
                messages.error(self.request,'کد شما یافت نشد')
                return redirect('checkout')
        messages.error(self.request,'مشکلی پیش آمد')
        return redirect('checkout')