from django.urls import path, include
from .views import show_products, ProductApiView, CategoryGenericApiView, CategoryDetailGenericApiView
from .views import CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', CategoryViewSet)


urlpatterns = [
    path('products/', show_products),
    path('api/products/', ProductApiView.as_view()),
    path('api/categories/statistics/', CategoryViewSet.as_view({'get': 'get_statistics'})),
    path('api/', include(router.urls)),
    # path('api/categories/', CategoryGenericApiView.as_view()),
    # path('api/categories/<int:pk>/', CategoryDetailGenericApiView.as_view()),
]
