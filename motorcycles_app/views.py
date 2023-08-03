from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Manufacturer, Motorcycle
from .serializer import ManufacturerSerializer, MotorcycleSerializer


# Create your views here.
@api_view(['GET'])
def get_all_manufacturers(request):
    queryset = Manufacturer.objects.all()
    data = ManufacturerSerializer(queryset, many=True).data
    return Response(data)


@api_view(['GET'])
def get_all_motorcycles(request):
    queryset = Motorcycle.objects.all()
    data = MotorcycleSerializer(queryset, many=True).data
    return Response(data)


@api_view(['POST'])
def new_manufacturer(request):
    serializer = ManufacturerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return Response({"error": "bad request"}, status=404)


@api_view(['POST'])
def new_motorcycle(request):
    serializer = MotorcycleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    return Response({"error": "bad request"}, status=404)


@api_view(['GET', 'PUT', 'DELETE'])
def manufacturer_by_pk(request, pk):
    method = request.method

    manufacturer = get_object_or_404(Manufacturer, pk=pk)

    if method == 'GET':
        data = ManufacturerSerializer(manufacturer).data
        return Response(data)

    if method == 'PUT':
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            manufacturer.name = request.data['name']
            manufacturer.country = request.data['country']
            manufacturer.founded = request.data['founded']
            manufacturer.save()
            data = ManufacturerSerializer(manufacturer).data
            return Response(data)
        return Response({"error": "bad request"}, status=404)

    if method == 'DELETE':
        manufacturer.delete()
        return Response({"message": f"Manufacturer id {pk} removed"})


@api_view(['GET', 'PUT', 'DELETE'])
def motorcycle_by_pk(request, pk):
    method = request.method

    motorcycle = get_object_or_404(Motorcycle, pk=pk)

    if method == 'GET':
        data = MotorcycleSerializer(motorcycle).data
        return Response(data)

    if method == 'PUT':
        serializer = MotorcycleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            motorcycle.manufacturer = Manufacturer.objects.get(
                pk=request.data['manufacturer'])
            motorcycle.model = request.data['model']
            motorcycle.year = request.data['year']
            motorcycle.engine_cc = request.data['engine_cc']
            motorcycle.type = request.data['type']
            motorcycle.color = request.data['color']
            motorcycle.save()
            data = MotorcycleSerializer(motorcycle).data
            return Response(data)
        return Response({"error": "bad request"}, status=404)

    if method == 'DELETE':
        motorcycle.delete()
        return Response({"message": f"Motorcycle id {pk} removed"})
