from typing import Iterable
from django.core import validators
from django.db import models
from django.utils.timezone import localtime
from accounts.models import User
from core.models import TimeStampModel
from products.models import Product, ProductAddon
from stores.models import Store

from django.utils.translation import gettext_lazy as _

class Cart(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='carts')
    
    class Meta:
        db_table = 'carts'
        managed = True
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

class CartItem(models.Model):
    #listagem dos produtos no carrinho
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        validators=[
            validators.MinValueValidator(1), 
            validators.MaxValueValidator(100)
        ]
    )
    
    @property
    def total_price(self):
        try:
            return self.product.price * self.quantity
        except:
            return 0
    
    class Meta:
        db_table = 'cart_items'
        managed = True
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'
        
class CartItemAddon(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_addon = models.ForeignKey(ProductAddon, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        validators=[
            validators.MinValueValidator(1),
        ], 
        default=1
    )

    def __str__(self):
        pass

    class Meta:
        db_table = 'cart_item_addons'
        managed = True
        verbose_name = 'CartItemAddon'
        verbose_name_plural = 'CartItemAddons'

class Order(TimeStampModel):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELED = 'canceled', 'Canceled'
        DELIVERED = 'delivered', 'Delivered'
        REFUNDED = 'refunded', 'Refunded'
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    
    class Meta:
        db_table = 'orders'
        managed = True
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    original_price = models.DecimalField(max_digits=12, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.PositiveIntegerField()
    
    @property
    def total_price(self):
        try:
            return self.price * self.quantity
        except:
            return 0
    
    class Meta:
        db_table = 'order_items'
        managed = True
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

class OrderItemAddon(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='addons')
    product_addon = models.ForeignKey(ProductAddon, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        validators=[
            validators.MinValueValidator(1),
        ]
    )
    
    @property
    def total_price(self):
        try:
            return self.product_addon.price * self.quantity
        except:
            return 0
    
    class Meta:
        db_table = 'order_item_addons'
        managed = True
        verbose_name = 'Order Item Addon'
        verbose_name_plural = 'Order Item Addons'

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    payment_method = models.CharField(max_length=64, default='credit')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20)
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    
    @property
    def created_at_regional(self):
        return localtime(self.created_at).strftime("%d/%m/%Y %H:%M:%S")
    
    @property
    def updated_at_regional(self):
        return localtime(self.updated_at).strftime("%d/%m/%Y %H:%M:%S")
    
    class Meta:
        db_table = 'payments'
        managed = True
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'