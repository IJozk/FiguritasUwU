from django.shortcuts import render, redirect
from .models import Pedido, detallePedido
from productos.models import Producto
from pedidos.carro import Carro
from django.http import HttpResponseRedirect

# Create your views here.


def nuevoPedido(request):

    detallePedido=detallePedido();

    productos = list(detallePedido.objects.select_related("pedido").filter(pedido__id=detallePedido.id))

    return render(request, 'pedidos/carrito_compra.html', {"productos":productos, })

def agregarProducto(request, prod_id, pagactual):
    carro=Carro(request)
    prod1=Producto.objects.get(id=prod_id)
    carro.agregar(producto=prod1)
    return redirect(pagactual)

def eliminarProducto(request, prod_id, pagactual):
    carro=Carro(request)
    prod=Producto.objects.get(id=prod_id)
    carro.eliminar(producto=prod)
    return redirect(pagactual)

def restarProducto(request, prod_id, pagactual):
    carro=Carro(request)
    prod=Producto.objects.get(id=prod_id)
    carro.restar_uprod(producto=prod)
    return redirect(pagactual)

def limpiarCarro(request, pagactual):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect(pagactual)