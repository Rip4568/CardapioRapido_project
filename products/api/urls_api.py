from django.urls import path, include
from rest_framework import routers

from products.api.viewsets import ProductViewSet, CategoryViewSet, ProductAddonViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'addons', ProductAddonViewSet, basename='addons')

urlpatterns = [
    path('', include(router.urls)),
]