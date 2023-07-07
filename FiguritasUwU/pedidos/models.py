from django.db import models
from productos.models import Producto
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField


# Create your models here.
User=get_user_model()

Estado =[
    ("P", "Preparando"),
    ("E", "Enviado"),
    ("R", "Recibido"),
    ("C", "Cancelado"),
]

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion_envio = models.CharField(max_length=200)
    estado = models.CharField(max_length=1, choices = Estado)
    
    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.detallePedido_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table='pedidos'
        verbose_name="pedido"
        verbose_name_plural='pedidos'
        ordering=['id']



class detallePedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    idpedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    cant = models.IntegerField(default=1)
   
    def __str__(self):
        return f'{self.cant} unidades de {self.producto.nombre}'
    
    class Meta:
        db_table='detalles'
        verbose_name="detalle"
        verbose_name_plural='detalles'
        ordering=['id']
