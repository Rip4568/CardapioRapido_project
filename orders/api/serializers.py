from rest_framework import serializers
from orders.models import (
    Cart,
    CartItem,
    CartItemAddon,
    Order,
    OrderItem,
    OrderItemAddon,
    Payment
)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        
class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartItemAddonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItemAddon
        fields = '__all__'

