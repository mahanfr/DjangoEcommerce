from django.urls import path
from .views import Management_index

urlpatterns = [
    path('', Management_index.as_view(), name='management-index'),
]