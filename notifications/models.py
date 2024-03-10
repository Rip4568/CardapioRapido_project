from django.db import models
from django.utils.timezone import localtime
from accounts.models import User
from orders.models import Order
from stores.models import Store
from django.utils.translation import gettext_lazy as _
        
        
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    
    @property
    def created_at_regional(self):
        return localtime(self.created_at).strftime("%d/%m/%Y %H:%M:%S")
    
    @property
    def updated_at_regional(self):
        return localtime(self.updated_at).strftime("%d/%m/%Y %H:%M:%S")
    
    def __str__(self):
        return self.title