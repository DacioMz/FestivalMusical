from django import forms
from . import models


class BandaForm(forms.ModelForm):
    class Meta:
        model= models.Banda
        fields= "__all__"

class EstiloForm(forms.ModelForm):
    class Meta:
        model= models.Estilo_Musical
        fields= "__all__"

class NacionalidadForm(forms.ModelForm):
    class Meta:
        model= models.Nacionalidad
        fields= "__all__"