from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    founded = models.IntegerField(null=True)

    def _str__(self):
        return self.name


class Motorcycle(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    year = models.IntegerField(null=True)
    engine_cc = models.IntegerField(null=True)
    type = models.CharField(max_length=30)
    color = models.CharField(max_length=100)

    def _str__(self):
        return f"{self.model} {self.manufacturer} {self.year} {self.engine_cc}"
