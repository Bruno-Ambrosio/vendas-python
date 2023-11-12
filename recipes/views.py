from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Produtos, Clientes
from .exceptions import CampoObrigatorioVazio, CadastroJaExiste
from .validations import ValidarCliente
from .services.cliente_service import ClienteService

cliente_srv = ClienteService()
validar_cliente = ValidarCliente()

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'home'
    })

def login(request):
    return render(
        request, 'recipes/pages/login.html', context={
        'name': 'login'
        }
    )

def menu(request):
    return render(
        request, 'recipes/pages/menu.html', context={
        'name': 'menu'
        }
    )

def lista_clientes(request):
    clientes = Clientes.objects.all()

def lista_produtos(request):
    produtos = Produtos.objects.all()
    produtos_dict = [{'nome': produto.descricao} for produto in produtos]

def cadastrar_cliente(request):
    if request.method == 'POST':
        try:
            cliente = cliente_srv.obter_objeto(request)
            validar_cliente.campos_obrigatorios(cliente)
            validar_cliente.campos_unicos(cliente)
            Clientes.objects.create(**cliente)
            return HttpResponse(f'Cliente salvo!\n"{cliente}"')
        except CampoObrigatorioVazio as e:
            return HttpResponseBadRequest(e)
        except CadastroJaExiste as e:
            return HttpResponseBadRequest(e)