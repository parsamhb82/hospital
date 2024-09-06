from django.db import models
from patient.models import Patient
from service.models import Service



class Reserve(models.Model):
    patinet = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    @property
    def patinets_name(self) -> str:
        return self.patinet.fullname
    @property
    def service_price(self):
        return self.service.price

    def __str__(self) -> str:
        return self.patinet.fullname
