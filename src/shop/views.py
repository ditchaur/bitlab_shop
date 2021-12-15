from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.db.models import Sum, Max, Min, Count, Avg
from drf_yasg.utils import swagger_auto_schema
from .models import Product, Category
from .serializers import ProductSerializer, ProductCreateSerializer, CategorySerializer, ProductDetailSerializer, CategoryAggregateSerializer
from .permissions import AdminPermission, ClientPermission
from .tasks import send_email


def show_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context=context)


class ProductApiView(APIView):
    permission_classes = (IsAuthenticated, ClientPermission)

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        # serializer = ProductDetailSerializer(products, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=ProductCreateSerializer)
    def post(self, request):
        data = request.data
        serializer = ProductCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        product = Product.objects.create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED, data=serializer.validated_data)


class CategoryGenericApiView(GenericAPIView, ListModelMixin, CreateModelMixin):
    permission_classes = (AllowAny, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryDetailGenericApiView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated, AdminPermission)
    serializer_class = CategorySerializer
    serializers = {
        'get_statistics': CategoryAggregateSerializer,
    }

    def get_statistics(self, request):
        queryset = self.get_queryset()
        queryset = queryset.aggregate(
            count=Count('id'),
            sum=Sum('product__price'),
            avg=Avg('product__price'),
            max=Max('product__price'),
            min=Min('product__price'),
        )
        serializer =self.serializers[self.action](queryset)
        send_email.delay('test_email@gmai.com', **serializer.data)
        return Response(status=status.HTTP_200_OK, data=serializer.data)