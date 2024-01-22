from django.shortcuts import render
from . import models

# Create your views here
def index(request):
    return render(request,"LineUp/index.html")

def Bandas_list(request):
    consulta = models.Banda.objects.all()
    contexto = {"Bandas": consulta}
    return render(request,"LineUp/Bandas_list.html",contexto)


def Estilo_musicales (request):
    consulta = models.Estilo_Musical.objects.all()
    contexto = {"Estilo": consulta}
    return render(request,"LineUp/Estilo_musicales.html",contexto)

def Nacionalidad (request):
    consulta = models.Nacionalidad.objects.all()
    contexto = {"Nacionalidad": consulta}
    return render(request,"LineUp/Nacionalidad.html",contexto)