from django.contrib.admin import ModelAdmin, register
from .models import Reserve

@register(Reserve)
class ReserveAdmin(ModelAdmin):
    list_display = ['patient', 'service', 'date', 'time']
    
