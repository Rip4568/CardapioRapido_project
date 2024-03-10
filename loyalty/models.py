from django.utils.timezone import localtime
from django.db import models
from accounts.models import User
from stores.models import Store
from orders.models import Order
from django.utils.translation import gettext_lazy as _

class UserLoyalty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='loyalty')
    current_count = models.PositiveIntegerField(default=1)
    total_orders = models.PositiveIntegerField(default=1)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='user_loyalties')
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    
    @property
    def created_at_regional(self):
        return localtime(self.created_at).strftime("%d/%m/%Y %H:%M:%S")
    
    @property
    def updated_at_regional(self):
        return localtime(self.updated_at).strftime("%d/%m/%Y %H:%M:%S")

    class Meta:
        db_table = 'user_loyalties'
        managed = True
        verbose_name = 'User Loyalty'
        verbose_name_plural = 'User Loyalties'