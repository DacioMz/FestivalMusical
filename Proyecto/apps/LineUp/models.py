from django.db import models

class Banda (models.Model):
    nombre= models.CharField(max_length=100)
    email= models.EmailField()
    miembros= models.PositiveIntegerField()

    def __str__ (self):
        return self.nombre

class Estilo_Musical (models.Model):
    estilo= models.CharField(max_length=100)

    def __str__ (self):
        return self.estilo

class Nacionalidad (models.Model):
     pais = models.CharField(max_length=100)

     def __str__ (self):
        return self.pais


