from django.shortcuts import render
from . import models

# Create your views here
def index(request):
    return render(request,"LineUp/index.html")

def Bandas_list(request):
    Bandas = models.Banda.objects.all()
    return render(request,"LineUp/Bandas_list.html", {"Banda": Bandas})