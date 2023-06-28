from django.contrib import admin
from  .models import Pedido, detallePedido

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    list_display=('id', 'direccion_envio', 'estado')
    search_fields=("id",)

class detallePedidoAdmin(admin.ModelAdmin):
    list_display=('idpedido', 'producto', 'cant')
    search_fields=("id",)   

admin.site.register(Pedido, PedidoAdmin)
admin.site.register(detallePedido, detallePedidoAdmin)
