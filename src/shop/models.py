from django.db import models
from django.contrib.auth.models import User
from . import Roles


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name='Описание', null=True, default='Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"Категория: {self.name}"


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30)
    price = models.IntegerField(verbose_name='Цена', default=100)
    description = models.TextField(verbose_name='Описание', null=True, default='Добавь описание')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты '

    def __str__(self):
        return f"Продукт: {self.name}"


class Role(models.Model):
    name = models.CharField(choices=Roles.choices, max_length=10)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
