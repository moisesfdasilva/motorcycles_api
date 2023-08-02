from rest_framework import serializers
from .models import Manufacturer, Motorcycle


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class MotorcycleSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(many=False, read_only=True)

    class Meta:
        model = Motorcycle
        fields = '__all__'
