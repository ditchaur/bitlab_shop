from django.urls import path
from .views import show_products, ProductApiView, CategoryGenericApiView, CategoryDetailGenericApiView


urlpatterns = [
    path('products/', show_products),
    path('api/products/', ProductApiView.as_view()),
    path('api/categories/', CategoryGenericApiView.as_view()),
    path('api/categories/<int:pk>/', CategoryDetailGenericApiView.as_view()),
]
