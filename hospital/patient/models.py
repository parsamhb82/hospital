from django.db import models

class Patient(models.Model):
    fullname = models.CharField(max_length=100)

    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.fullname
