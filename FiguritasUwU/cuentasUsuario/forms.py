from django import forms
from django.contrib.auth.forms import UserCreationForm

class FormularioNuevoCliente(UserCreationForm):
    pass



class FormularioModCliente(UserCreationForm):
    username=forms.CharField(disabled=True)
    password=forms.CharField(widget=forms.PasswordInput)
    pass