from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('Bandas_list', views.Bandas_list, name="Bandas_list"),
    path('Estilo_musicales', views.Estilo_musicales, name="Estilo_musicales"),
    path('Nacionalidad', views.Nacionalidad, name="Nacionalidad"),
    path('Banda_forms', views.Banda_forms, name="Banda_forms"),
    path('Estilo_musical', views.Estilos_forms, name="Estilo_forms"),
    path('Nacionalidad_forms', views.Nacionalidad_forms, name="Nacionalidad_forms"),
     ]
