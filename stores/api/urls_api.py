from django.urls import path, include
from rest_framework import routers
from .viewsets import StoreViewSet

router = routers.DefaultRouter()
router.register('stores', StoreViewSet, basename='Store')

urlpatterns = [
    path('', include(router.urls)),
]