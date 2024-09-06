from django.contrib.admin import register, ModelAdmin
from .models import Patient

@register(Patient)
class PatientAdmin(ModelAdmin):
    pass