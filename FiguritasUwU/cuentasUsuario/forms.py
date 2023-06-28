from django import forms

class FormularioNuevoCliente(forms.Form):

    nombreUsuario=forms.CharField()
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    contrasenia=forms.CharField(widget=forms.PasswordInput)
    direccion = forms.CharField()
    telefono = forms.CharField()
    ciudad = forms.CharField()
    pais =forms.CharField()



    