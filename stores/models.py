import calendar
from operator import index
from wsgiref.validate import validator
from django.core import validators
from django.db import models

from django.db import models
from django.utils.text import slugify
from django.utils.timezone import localtime
from accounts.models import User
from django.utils.translation import gettext_lazy as _

class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(_("Nome da loja"),max_length=64, db_index=True, unique=True)
    cpf = models.CharField(max_length=32, unique=True, null=True, blank=True)
    cnpj = models.CharField(max_length=32, unique=True, null=True, blank=True)
    banner = models.ImageField(_("Banner da loja"), upload_to='stores/banners/', null=True, blank=True)
    logo = models.ImageField(_("Logo da loja"), upload_to='stores/logos/', null=True, blank=True)
    description = models.CharField(_("Descrição da loja"),max_length=255, null=True, blank=True)
    activate_loyalty = models.BooleanField(_("Ativar Fidelidade ?:"),default=False)
    slug = models.SlugField(_("Slug da loja para o redirecionamento, sera criado auto."), unique=True, blank=True, null=True, editable=False)
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    
    @property
    def created_at_regional(self):
        return localtime(self.created_at).strftime("%d/%m/%Y %H:%M:%S")
    
    @property
    def updated_at_regional(self):
        return localtime(self.updated_at).strftime("%d/%m/%Y %H:%M:%S")
    
    def __str__(self):
        return str(_(self.name))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return f"/store/{self.slug}/"
    
    class Meta:
        db_table = 'stores'
        managed = True
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'

class AddressStore(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    reference_point = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=16, null=True, blank=True)
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
        db_table = 'addresses_store'
        managed = True
        verbose_name = 'Address Store'
        verbose_name_plural = 'Addresses Stores'

class OpeningHours(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='opening_hours')
    day_of_week = models.PositiveSmallIntegerField(
        _("Dia da semana, 1 para domingo e 7 para sábado"),
        unique=True, 
        validators=[
            validators.MinValueValidator(1), 
            validators.MaxValueValidator(7)
        ]
    )
    is_open = models.BooleanField(_("Esta aberto ?: "),default=False)
    
    opening_time = models.TimeField(_("Horario de abertura: ") ,null=True, blank=True)
    closing_time = models.TimeField(_("Horario de fechamento: "), null=True, blank=True)
    
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    
    @property
    def created_at_regional(self):
        return localtime(self.created_at).strftime("%d/%m/%Y %H:%M:%S")
    
    @property
    def updated_at_regional(self):
        return localtime(self.updated_at).strftime("%d/%m/%Y %H:%M:%S")
    
    def __str__(self) -> str:
        return str(_(calendar.day_name[self.day_of_week - 2]))
    
    class Meta:
        db_table = 'opening_hours'
        managed = True
        verbose_name = 'Opening Hours'
        verbose_name_plural = 'Opening Hours'