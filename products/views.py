from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product , Category
from django.views.generic import ListView , View
from django.db.models import Q
from django.core.paginator import Paginator

class ProductsView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    # TODO: Make This number Higher
    paginate_by = 30

class ProductView(View):
    def get(self,*args,**kwargs):
        context = {
            'product' : get_object_or_404(Product,id=kwargs['product_id'])
        }
        return render(self.request,'products/product.html',context=context)

class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'