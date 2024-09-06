from django.db import models
from patient.models import Patinet
from service.models import Service


class Reserve(models.Model):
    patinet = models.ForeignKey(Patinet, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def patinet_name(self) -> str:
        return self.patinet.fullname
    
    def service_price(self):
        return self.service.price

    def __str__(self) -> str:
        return self.patinet
