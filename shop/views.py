from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from .models import Product
from .serializers import ProductSerializer, ProductCreateSerializer


def show_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context=context)


class ProductApiView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        products = Product.objects.all()
        print(products)
        serializer = ProductSerializer(products, many=True)
        print(serializer.data)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        data = request.data
        serializer = ProductCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        product = Product.objects.create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED, data=serializer.validated_data)
