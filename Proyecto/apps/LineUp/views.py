from django.shortcuts import render
from . import models

# Create your views here
def index(request):
    return render(request,"LineUp/index.html")

def Bandas_list(request):
    consulta = models.Banda.objects.all()
    contexto = {"Bandas": consulta}
    return render(request,"LineUp/Bandas_list.html",contexto)