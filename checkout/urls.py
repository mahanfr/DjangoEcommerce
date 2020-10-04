from django.urls import path
from .views import CheckoutView , SubmitPromoView

urlpatterns = [
    path('', CheckoutView.as_view() , name='checkout'),
    path('Promo-submit',SubmitPromoView.as_view(),name ='promo-submit'),
]