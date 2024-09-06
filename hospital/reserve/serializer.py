from rest_framework.serializers import ModelSerializer
from .models import *

class ReserveSerializer(ModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'

class ReserveListSerializer(ModelSerializer):
    class Meta:
        model = Reserve
        fields = ['id', 'patinet_name', 'date', 'time', 'service']