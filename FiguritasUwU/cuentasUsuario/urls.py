from django.urls import path, include
from cuentasUsuario import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('formcli/', views.cliente, name='formcli'),
]
