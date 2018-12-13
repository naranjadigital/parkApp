from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Distrito(models.Model):
    nombre = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Estacionamiento(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80, null=True, blank=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=7)
    longitud = models.DecimalField(max_digits=9, decimal_places=7)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE, null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
