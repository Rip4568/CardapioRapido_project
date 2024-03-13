from django.contrib import admin

from .models import Category, Product, ProductAddon
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'store', 'price', 'active')
    list_filter = ('active', 'category', 'store')
    search_fields = ('name', 'category', 'store')
    list_editable = ('active',)
    list_per_page = 30
    list_display_links = ('name', 'category', 'store')
    
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'store', 'price', 'active', 'image')
        }),
    )

admin.site.register(Category)
admin.site.register(ProductAddon)
admin.site.register(Product, ProductAdmin)
