from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from shop.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'category_id')

    def validate(self, attrs):
        if attrs['price'] <= 0:
            raise ValidationError("Price is invalid.")
        if attrs['category_id'] <= 0:
            raise ValidationError("Category id is invalid.")
        if not Category.objects.filter(id=attrs['category_id']):
            raise ValidationError("Category id not found.")
        return attrs


class ProductDetailSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    category = CategorySerializer()