from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    founded = models.IntegerField
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str__(self):
        return self.name


class Motorcycle(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    year = models.IntegerField
    engine_cc = models.IntegerField
    type = models.CharField(max_length=30)
    color = models.CharField(max_length=100)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str__(self):
        return f"{self.model} {self.manufacturer} {self.year} {self.engine_cc}"
