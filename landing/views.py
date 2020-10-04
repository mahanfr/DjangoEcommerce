from django.shortcuts import render
from products.models import Product

# Create your views here.
def index(request):
    context = {
        'products' : Product.objects.all(),
    }
    return render(request,'landing/index.html',context=context)

def about(request):
    return render(request,'landing/about.html')

def support(request):
    return render(request,'landing/support.html')