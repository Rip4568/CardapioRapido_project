from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import localtime
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampModel


class User(AbstractUser):
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True, blank=True, null=True)
    newsletter = models.BooleanField(_("Newsletter"), default=False)
    email = models.EmailField(_("Email"), unique=True)
    phone_number = models.CharField(max_length=16, unique=True, null=False)
    name = models.CharField(_("Name"), max_length=255, null=True, blank=True)
    
    @property
    def created_at_regional(self):
        return localtime(self.created_at).strftime("%d/%m/%Y %H:%M:%S")
    
    @property
    def updated_at_regional(self):
        return localtime(self.updated_at).strftime("%d/%m/%Y %H:%M:%S")
    
    def __str__(self) -> str:
        return self.username or self.email
    
    
class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    street_address = models.CharField(_("Endereço da Rua"), max_length=255)
    reference_point = models.CharField(
        _("Ponto de Referencia perto da localizacao da casa"), 
        max_length=255, 
        null=True, 
        blank=True
    )
    city = models.CharField(
        _("Cidade em que hospeda"),
        max_length=64
    )
    state = models.CharField(_("Estado em que esta localizado"), max_length=64)
    postal_code = models.CharField(
        _("Codigo Postal"), 
        max_length=16, 
        null=True, 
        blank=True
    )
    country = models.CharField(max_length=32, default='Brasil')
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    
    @property
    def created_at_regional(self):
        return localtime(self.created_at).strftime("%d/%m/%Y %H:%M:%S")
    
    @property
    def updated_at_regional(self):
        return localtime(self.updated_at).strftime("%d/%m/%Y %H:%M:%S")
    
    class Meta:
        db_table = 'addresses_user'
        managed = True
        verbose_name = 'Addresses User'
        verbose_name_plural = 'Addresses Users'