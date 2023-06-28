from django.shortcuts import render
from .models import Pedido, detallePedido
from django.db.models import Q

# Create your views here.


def carrito(request):

    productos = list(detallePedido.objects.select_related("producto").filter(pedido__id=))

    return render(request, 'pedidos/carrito_compra.html', {"productos":productos, })
