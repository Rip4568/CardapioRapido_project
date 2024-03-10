from django.core import validators
from django.db import models
from django.utils.timezone import localtime
from accounts.models import User
from products.models import Product
from stores.models import Store
from django.utils.translation import gettext_lazy as _
    
    
class ReviewProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    rating = models.PositiveIntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])
    comment = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    
    @property
    def created_at_regional(self):
        return localtime(self.created_at).strftime("%d/%m/%Y %H:%M:%S")
    
    @property
    def updated_at_regional(self):
        return localtime(self.updated_at).strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return f"{self.user.name} | {self.product.name} | {self.rating}"

    class Meta:
        db_table = 'reviews_product'
        managed = True
        verbose_name = 'ReviewProduct'
        verbose_name_plural = 'ReviewProducts'

class ReviewStore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_stores')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    rating = models.PositiveIntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)])
    comment = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    
    @property
    def created_at_regional(self):
        return localtime(self.created_at).strftime("%d/%m/%Y %H:%M:%S")
    
    @property
    def updated_at_regional(self):
        return localtime(self.updated_at).strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return f"{self.user.name} | {self.store} | {self.rating}"

    class Meta:
        db_table = 'reviews_store'
        managed = True
        verbose_name = 'ReviewStore'
        verbose_name_plural = 'ReviewStores'