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
