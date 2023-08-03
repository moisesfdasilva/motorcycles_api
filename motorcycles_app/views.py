from rest_framework.decorators import api_view
from rest_framework.response import Response
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
