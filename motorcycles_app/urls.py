from django.urls import path
from .apiviews import ManufacturerList, MotorcycleList


urlpatterns = [
    path("manufacturer/", ManufacturerList.as_view(), name="polls_list"),
    path("motorcycle/", MotorcycleList.as_view(), name="polls_detail")
]
