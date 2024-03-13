from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from .viewsets import OrderViewSet, CartViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'carts', CartViewSet, basename='carts')

urlpatterns = [
    path('', include(router.urls)),
]