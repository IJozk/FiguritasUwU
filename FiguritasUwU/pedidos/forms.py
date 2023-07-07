from django import forms
from .models import detallePedido, Pedido

class pedidoForm(forms.ModelForm):
    class Meta:
        model= Pedido
        fields= '__all__'

class detallePedidoForm(forms.ModelForm):
    class Meta:
        model= detallePedido
        fields= '__all__'