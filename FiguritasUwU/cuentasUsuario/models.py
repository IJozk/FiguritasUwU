from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombreUsuario=models.CharField(max_length=50, null=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    contrasenia = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200, verbose_name="Dirección cliente")
    telefono = models.CharField(max_length=9)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

