from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from products.api.serializers import ProductSerializer, CategorySerializer, ProductAddonSerializer

from products.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = CategorySerializer


class ProductAddonViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductAddonSerializer