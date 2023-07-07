from django.urls import path
from .views import anime, marvelDc, comic, otros, manga, producto, agregar_producto, listar_productos, modificar_producto, eliminar_producto


urlpatterns = [
    path('anime/', anime , name='anime'),
    path('marvelDc/', marvelDc , name='marvelDc'),
    path('comic/', comic , name='comic'),
    path('manga/', manga , name='manga'),
    path('otros/', otros , name='otros'),
    path('producto/<int:idprod>/', producto, name='producto'),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name= "listar_productos"),
    path('modificar-producto/<id>', modificar_producto,name="modificar_producto"),
    path('eliminar-producto/<id>', eliminar_producto,name="eliminar_producto"),

]
