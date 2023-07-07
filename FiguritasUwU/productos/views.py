from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.db.models import Q
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def anime(request):

    productos = list(Producto.objects.select_related("categoria").filter(categoria__nombre='FIGURA ANIME'))

    return render(request, 'productos/anime.html', {"productos":productos, })

def manga(request):

    productos = list(Producto.objects.select_related("categoria").filter(categoria__nombre='MANGA'))

    return render(request, 'productos/manga.html', {"productos":productos, })

def comic(request):

    productos = list(Producto.objects.select_related("categoria").filter(categoria__nombre='COMIC'))

    return render(request, 'productos/comic.html', {"productos":productos, })

def marvelDc(request):

    productos = list(Producto.objects.select_related("categoria").filter(Q(categoria__nombre='FIGURA MARVEL') | Q(categoria__nombre='FIGURA DC')))

    return render(request, 'productos/marvelDc.html', {"productos":productos, })

def otros(request):

    productos = list(Producto.objects.select_related("categoria").filter(categoria__nombre='POSTER'))

    return render(request, 'productos/otros.html', {"productos":productos, })



def producto(request, idprod):

    producto = Producto.objects.get(id=idprod)

    return render(request, 'productos/producto.html', {"producto":producto, })

# Create your views here.
@login_required
def agregar_producto(request):
    if request.user.is_superuser:
        data={
            'form': ProductoForm()
        }
        
        if request.method == 'POST':
            formulario = ProductoForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
            else:
                data["form"] = formulario

        return render(request, 'productos/agregar.html',data)


@login_required
def listar_productos(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
        
        return render(request, 'productos/listar.html', {'productos': productos})

@login_required
def modificar_producto(request, id):
    if request.user.is_superuser:
        producto = get_object_or_404(Producto, id=id)
        
        data = {
            'form': ProductoForm(instance=producto)
        }
        
        if request.method == 'POST':
            formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect(to="listar_productos")
            data["form"] = formulario
        
        return render(request,'productos/modificar.html', data)

@login_required
def eliminar_producto(request, id):
    if request.user.is_superuser:
        producto = get_object_or_404(Producto, id=id)
        producto.delete()
        return redirect(to="listar_productos")

