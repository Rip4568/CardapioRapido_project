from django.db import models
from django.utils.timezone import localtime
from stores.models import Store
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=64)
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    
    @property
    def created_at_regional(self):
        return localtime(self.created_at).strftime("%d/%m/%Y %H:%M:%S")
    
    @property
    def updated_at_regional(self):
        return localtime(self.updated_at).strftime("%d/%m/%Y %H:%M:%S")
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categories'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=64)
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    last_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='product_images')
    
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    
    @property
    def created_at_regional(self):
        return localtime(self.created_at).strftime("%d/%m/%Y %H:%M:%S")
    
    @property
    def updated_at_regional(self):
        return localtime(self.updated_at).strftime("%d/%m/%Y %H:%M:%S")
    
    def __str__(self):
        return f'{self.name} | {self.store} | {self.category} {self.price}'
    
    class Meta:
        db_table = 'products'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    

class ProductAddon(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='addons')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    
    @property
    def created_at_regional(self):
        return localtime(self.created_at).strftime("%d/%m/%Y %H:%M:%S")
    
    @property
    def updated_at_regional(self):
        return localtime(self.updated_at).strftime("%d/%m/%Y %H:%M:%S")
    
    class Meta:
        db_table = 'product_addons'
        managed = True
        verbose_name = 'Product Addon'
        verbose_name_plural = 'Product Addons'