from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('landing.urls')),
    path('products/',include('products.urls')),
    path('cart/',include('cart.urls')),
    path('users/',include('users.urls')),
    path('checkout/',include('checkout.urls')),
    path('management/',include('management.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
