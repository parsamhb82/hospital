from django.contrib.admin import register, ModelAdmin
from .models import Service

@register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ['name', 'description', 'price']