from django.shortcuts import render
from .models import Pedido, detallePedido
from django.db.models import Q

# Create your views here.


def nuevoPedido(request):

    detallePedido=detallePedido();

    productos = list(detallePedido.objects.select_related("pedido").filter(pedido__id=detallePedido.id))

    return render(request, 'pedidos/carrito_compra.html', {"productos":productos, })
