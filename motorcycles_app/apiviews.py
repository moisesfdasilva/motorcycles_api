from rest_framework import generics
from .models import Manufacturer, Motorcycle
from .serializer import ManufacturerSerializer, MotorcycleSerializer


class ManufacturerList(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class MotorcycleList(generics.ListCreateAPIView):
    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer
