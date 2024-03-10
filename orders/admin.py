from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem, OrderItemAddon, Payment, CartItemAddon

class CartItemAddonInline(admin.TabularInline):
    model = CartItemAddon
    extra = 1

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    readonly_fields = ('total_price',)

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline, CartItemAddonInline]
    list_display = ('user', 'store', 'created_at_regional', 'updated_at_regional')
    list_filter = ('user', 'store')

class OrderItemAddonInline(admin.TabularInline):
    model = OrderItemAddon
    extra = 1

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('total_price', 'original_price')
    #inlines = [OrderItemAddonInline]

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline, OrderItemAddonInline]
    list_display = ('user', 'store', 'status', 'created_at_regional', 'updated_at_regional')
    list_filter = ('user', 'store', 'status')
    readonly_fields = ('created_at_regional', 'updated_at_regional')

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 1
    readonly_fields = ('created_at_regional', 'updated_at_regional')

admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)