from django.urls import path
from .views import get_all_manufacturers, get_all_motorcycles


urlpatterns = [
    path("manufacturer/all", get_all_manufacturers, name="manufacturers_list"),
    path("motorcycle/all", get_all_motorcycles, name="motorcycles_detail")
]
