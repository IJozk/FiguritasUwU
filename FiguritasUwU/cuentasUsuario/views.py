from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from cuentasUsuario.forms import FormularioNuevoCliente
from cuentasUsuario.models import Cliente
from django.contrib import messages



# Create your views here.


def index(request):

    return render(request, "cuentasUsuario/index.html")

def cliente(request):

    if request.method=="POST":


        miForm=FormularioNuevoCliente(request.POST)

        if miForm.is_valid():

            infForm=miForm.cleaned_data

            cli=Cliente()

            cli.nombreUsuario = infForm['nombreUsuario']
            cli.nombre = infForm['nombre']
            cli.apellido = infForm['apellido']
            cli.email = infForm['email']
            cli.contrasenia = infForm['contrasenia']
            cli.direccion = infForm['direccion']
            cli.telefono = infForm['telefono']
            cli.ciudad = infForm['ciudad']
            cli.pais = infForm['pais']

            cli.save()

            return render(request, "cuentasUsuario/guardado.html" )
        
        else: 
            return render(request, "cuentasUsuario/malo.html" )
        
    else:

        miForm=FormularioNuevoCliente()

    return render(request, "cuentasUsuario/formularioCli.html", {"form": miForm})

