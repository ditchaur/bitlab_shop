from django.urls import path
from .views import show_products, ProductApiView


urlpatterns = [
    path('products/', show_products),
    path('api/products/', ProductApiView.as_view()),
]
