from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'message', 'created_at_regional']
    list_filter = ['created_at', 'is_read']
    list_display_links = ['user', 'title']
    list_per_page = 30
    
admin.site.register(Notification, NotificationAdmin)