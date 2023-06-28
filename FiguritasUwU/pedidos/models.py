from django.db import models
from productos.models import Producto


# Create your models here.

Estado =[
    ("P", "Preparando"),
    ("E", "Enviado"),
    ("R", "Recibido"),
    ("C", "Cancelado"),
]

class Pedido(models.Model):
    cliente = models.CharField(max_length=50)
    direccion_envio = models.CharField(max_length=200)
    estado = models.CharField(max_length=1, choices = Estado)

class detallePedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    idpedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    cant = models.IntegerField()