from rest_framework.serializers import ModelSerializer
from .models import Service
from reserve.models import Reserve


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class SuperUserReserveSerializer(ModelSerializer):
    class Meta:
        model = Reserve
        fields = ["id", "patinet_name", "date", "time", "service", "service_price"]
