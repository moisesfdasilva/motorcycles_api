from django.urls import path
from . import views


urlpatterns = [
    path("manufacturer/all", views.get_all_manufacturers),
    path("motorcycle/all", views.get_all_motorcycles),
    path("manufacturer/new", views.new_manufacturer),
    path("motorcycle/new", views.new_motorcycle),
    path("manufacturer/<int:pk>", views.manufacturer_by_pk),
    path("motorcycle/<int:pk>", views.motorcycle_by_pk),
]
