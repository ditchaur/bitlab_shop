from django.shortcuts import render, redirect
from .models import Product


def show_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context=context)
