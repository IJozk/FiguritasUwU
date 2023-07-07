from django.urls import path
from pedidos import views


app_name="carro"

urlpatterns = [
    path("agregar/<int:prod_id>/<pagactual>", views.agregarProducto, name="agregar"),
    path("eliminar/<int:prod_id>/<pagactual>", views.eliminarProducto, name="eliminar"),
    path("restar/<int:prod_id>/<pagactual>", views.restarProducto, name="restar"),
    path("limpiar/<pagactual>", views.limpiarCarro , name="limpiar"),
]
