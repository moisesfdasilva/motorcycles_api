from rest_framework import serializers
from .models import Manufacturer, Motorcycle


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class MotorcycleSerializer(serializers.ModelSerializer):
    manufacturer = serializers.PrimaryKeyRelatedField(
        queryset=Manufacturer.objects.all(), many=False)

    class Meta:
        model = Motorcycle
        fields = '__all__'
