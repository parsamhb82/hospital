from django.contrib.admin import ModelAdmin, register
from .models import Reserve

@register(Reserve)
class ReserveAdmin(ModelAdmin):
    pass
    
