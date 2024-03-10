from django.contrib import admin
from .models import User, UserAddress

class UserAddressInline(admin.StackedInline):
    model = UserAddress
    extra = 1
    
class UserAdmin(admin.ModelAdmin):
    inlines = [UserAddressInline]
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_active', 'is_staff', 'is_superuser']
    list_display_links = ['username', 'email']
    list_per_page = 30
    
admin.site.register(User, UserAdmin)
