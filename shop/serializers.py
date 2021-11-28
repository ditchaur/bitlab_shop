from rest_framework.serializers import ModelSerializer, IntegerField
from shop.models import Product, Category


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateSerializer(ModelSerializer):
    category_id = IntegerField()

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'category_id')


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'