from django.shortcuts import render
from .models import Producto
from django.db.models import Q

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

