from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from cuentasUsuario.forms import FormularioNuevoCliente, FormularioModCliente
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from pedidos.carro import Carro




# Create your views here.


def index(request):
    carro=Carro(request)

    return render(request, "cuentasUsuario/index.html")
"{% url 'formcli' %}"


def cliente(request):
    data={
        "form": FormularioNuevoCliente()
    }
    if request.method=="POST":

        miForm=FormularioNuevoCliente(data=request.POST)

        if miForm.is_valid():
            miForm.save()
            user = authenticate(username=miForm.cleaned_data["username"], password=miForm.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect("index")
        data["form"]=miForm
        
    return render(request, "cuentasUsuario/formularioCli.html", data)

@login_required
def tablaCliente(request):
    if request.user.is_superuser:
        clientes=list(User.objects.all())

        return render(request, 'cuentasUsuario/tablaCli.html', {"clientes":clientes, })

def eliminarCliente(request, usuario):

    cli=User.objects.get(username=usuario)

    cli.delete()

    return redirect("tablaCli")



def modCliente(request, usuario):
    cli = get_object_or_404(User, username=usuario)
    if request.method=="POST":

        miForm=FormularioModCliente(request.POST, instance=cli)

        if miForm.is_valid():
            cli = miForm.save(commit=False)
            cli.save()

            return render(request, "cuentasUsuario/guardado.html" )
        
        else: 
            return render(request, "cuentasUsuario/malo.html" )
        
    else:

        miForm=FormularioModCliente(instance=cli)

    return render(request, "cuentasUsuario/formModCli.html", {"form": miForm})

