from django.shortcuts import render, redirect
from .models import Pedido, detallePedido
from productos.models import Producto
from pedidos.carro import Carro
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import pedidoForm, detallePedidoForm
from django.contrib.auth.models import User

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

def nuevoPedido(request, productos, cantidad):
    pedido=Pedido(User.username, 'direccion x', "P")
    data={
            'productos':productos
        }
    for prod in productos:
            detalle=detallePedido(prod.id, pedido.id, cantidad)


    if request.method == 'POST':
                pedido.save()
                detalle.save()

    return render(request, 'pedidos/confirmarPedido.html',data)