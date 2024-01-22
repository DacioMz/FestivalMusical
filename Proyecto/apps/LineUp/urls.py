from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Bandas_list', views.Bandas_list, name="Bandas_list"),
]
