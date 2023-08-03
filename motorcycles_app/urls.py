from django.urls import path
from .views import ManufacturerList, MotorcycleList


urlpatterns = [
    path("manufacturer/all", ManufacturerList.as_view(), name="polls_list"),
    path("motorcycle/all", MotorcycleList.as_view(), name="polls_detail")
]
