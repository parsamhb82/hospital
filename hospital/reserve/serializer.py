from rest_framework.serializers import ModelSerializer
from .models import *

class ReserveSerializer(ModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'