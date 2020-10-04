from django.urls import path
from . import views

urlpatterns = [
    path('',views.OrderSummaryView.as_view(),name='order-summary'),
    path('add-to-cart/<int:product_id>',views.add_to_cart,name='add-to-cart'),
    path('remove-from-cart/<int:product_id>',views.remove_from_cart,name='remove-from-cart'),
    path('Delete-product-from-cart/<int:product_id>',views.Delete_product_from_cart,name='Delete-product-from-cart'),
]