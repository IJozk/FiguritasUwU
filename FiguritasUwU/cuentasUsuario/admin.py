from django.contrib import admin
from  cuentasUsuario.models import Cliente

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=('id', 'nombre', 'apellido')
    search_fields=("id",)

admin.site.register(Cliente, ClientesAdmin)

