from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail


# Create your views here.


def index(request):

    return render(request, "cuentasUsuario/index.html")

