from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre= models.CharField(max_length=50)

    class Meta: 
        verbose_name="categoria"
        verbose_name="categorias"

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta: 
        verbose_name="marca"
        verbose_name="marcas"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    stock= models.IntegerField(null=True)

    class Meta: 
        verbose_name="producto"
        verbose_name="productos"

    def __str__(self):
        return self.nombre
