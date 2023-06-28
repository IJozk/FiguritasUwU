from django.contrib import admin
from  .models import Producto, Categoria, Marca

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=('id', 'imagen','nombre', 'marca', 'precio', 'categoria')
    search_fields=("nombre", 'categoria')

class MarcaAdmin(admin.ModelAdmin):
    list_display=('nombre',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nombre',)


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)
