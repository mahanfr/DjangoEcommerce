from django.urls import path
from .views import ProductsView, ProductView , CategoryListView

urlpatterns = [
    path('', ProductsView.as_view(), name='allproducts'),
    path('<int:product_id>/', ProductView.as_view(), name='product'),
    path('categories',CategoryListView.as_view(),name='categories')
]