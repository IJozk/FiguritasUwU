from django.urls import path, include
from cuentasUsuario import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('formcli/', views.cliente, name='formcli'),
    path('tablaCli/', views.tablaCliente, name='tablaCli'),
    path('eliminarCli/<usuario>', views.eliminarCliente, name='eliminarCli'),
    path('modCli/<usuario>', views.modCliente, name='modCli'),
]
