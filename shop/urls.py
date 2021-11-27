from django.urls import path
from .views import show_products


urlpatterns = [
    path('products/', show_products),
]
