from django.shortcuts import redirect, render
from . import models
from . import forms 

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


def Banda_forms (request):
    if request.method == "POST":
        form =forms.BandaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("Bandas_list")
    else:
        form =forms.BandaForm()
    return render(request,"LineUp/Banda_forms.html",{"form": form})

def Estilos_forms (request):
    if request.method == "POST":
        form =forms.EstiloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("Estilo_musicales")
    else:
        form =forms.EstiloForm()
    return render(request,"LineUp/Estilo_forms.html",{"form": form})    


def Nacionalidad_forms (request):
    if request.method == "POST":
        form =forms.NacionalidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("Nacionalidades")
    else:
        form =forms.NacionalidadForm()
    return render(request,"LineUp/Nacionalidad_forms.html",{"form": form})    