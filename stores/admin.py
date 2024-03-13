from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.db.models import Avg, Count
from .models import Store, OpeningHours, AddressStore
from reviews.models import ReviewStore, ReviewProduct
from products.models import Product, Category

class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1

class ReviewStoreInline(admin.TabularInline):
    model = ReviewStore
    extra = 1
    readonly_fields = ('rating', 'comment', 'user', 'created_at', 'updated_at')

class ReviewProductInline(admin.StackedInline):
    model = ReviewProduct
    extra = 1
    readonly_fields = ('rating', 'comment', 'user', 'created_at', 'updated_at')
    fk_name = 'product'

class ProductInline(admin.TabularInline):
    model = Product
    extra = 1

class OpeningHoursInline(admin.TabularInline):
    model = OpeningHours
    extra = 1

class AddressStoreInline(admin.StackedInline):
    model = AddressStore
    extra = 1

class StoreAdmin(admin.ModelAdmin):
    inlines = [OpeningHoursInline, AddressStoreInline, ProductInline, ReviewStoreInline, CategoryInline]
    list_display = ['name', 'user', 'created_at_regional', 'average_rating', 'total_products', 'total_reviews']
    list_filter = ['created_at', 'activate_loyalty']
    list_display_links = ['name', 'user']
    list_per_page = 30

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _total_products=Count('products', distinct=True),
            _total_reviews=Count('reviews', distinct=True),
            _average_rating=Avg('reviews__rating')
        )
        return queryset

    def total_products(self, obj):
        return obj._total_products
    total_products.short_description = _('Total de Produtos')

    def total_reviews(self, obj):
        return obj._total_reviews
    total_reviews.short_description = _('Total de Avaliações')

    def average_rating(self, obj):
        return obj._average_rating
    average_rating.short_description = _('Média de Avaliações')

admin.site.register(Store, StoreAdmin)

admin.site.register(AddressStore)