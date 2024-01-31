from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from .models import Clientes


class ClientesFilterForm(BSModalForm):
    type = forms.ChoiceField(choices=Clientes.TYPE_GENER)

    class Meta:
        fields = ['type']


class ClientesModelForm(BSModalModelForm):
    
    nombre = forms.CharField(min_length=3,max_length=50)
    apellido = forms.CharField(min_length=3,max_length=50)
   
    class Meta:

        model = Clientes
        fields =['nombre','apellido','telefono','email','direccion','type_genero']

        widgets = {
          "email":forms.EmailInput(), 
          "telefono":forms.NumberInput()
        }

class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']