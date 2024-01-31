from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import (
    ClientesFilterForm,
    ClientesModelForm,
    CustomAuthenticationForm,
    CustomUserCreationForm
)
from .models import Clientes


class Index(generic.ListView):
    model = Clientes
    context_object_name = 'clientes'
    template_name = 'index.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if 'type' in self.request.GET:
            qs = qs.filter(type_genero=int(self.request.GET['type']))
        return qs


class ClientesFilterView(BSModalFormView):
    template_name = 'examples/filter_client.html'
    form_class =  ClientesFilterForm

    def form_valid(self, form):
        self.filter = '?type=' + form.cleaned_data['type']
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('index') + self.filter


class ClienteCreateView(BSModalCreateView):
    template_name = 'examples/create_client.html'
    form_class =  ClientesModelForm
    success_message = 'Success: Cliente creado.'
    success_url = reverse_lazy('index')


class ClienteUpdateView(BSModalUpdateView):
    model = Clientes
    template_name = 'examples/update_client.html'
    form_class = ClientesModelForm
    success_message = 'Success: Cliente modificado.'
    success_url = reverse_lazy('index')


class ClienteReadView(BSModalReadView):
    model = Clientes
    template_name = 'examples/read_client.html'
    

class ClienteDeleteView(BSModalDeleteView):
    model = Clientes
    template_name = 'examples/delete_client.html'
    success_message = 'Success: Cliente eliminado.'
    success_url = reverse_lazy('index')


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'examples/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('index')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'examples/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('index')


def clientes(request):
    data = dict()
    if request.method == 'GET':
        clientes = Clientes.objects.all()
        data['table'] = render_to_string(
            '_clients_table.html',
            {'clientes': clientes},
            request=request
        )
        return JsonResponse(data)

# Create your views here.
