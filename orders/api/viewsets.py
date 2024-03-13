from rest_framework import viewsets
from rest_framework.response import Response

from orders.api.serializers import OrderSerializer, CartSerializer

from orders.models import Order, Cart

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class CartViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
