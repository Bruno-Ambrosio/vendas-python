from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Produtos, Clientes
from .exceptions import CampoObrigatorioVazio, CadastroJaExiste
from .validations import ValidarCliente
from .utils import ClienteUtils

cliente_utils = ClienteUtils()
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

def cliente_cadastro(request):
    return render(
        request, 'recipes/pages/cliente/cadastro.html', context={
        'name': 'cliente_cadastro'
        }
    )
    
def fornecedor_cadastro(request):
    return render(
        request, 'recipes/pages/fornecedor/cadastro.html', context={
        'name': 'fornecedor_cadastro'
        }
    )
    
def funcionario_cadastro(request):
    return render(
        request, 'recipes/pages/funcionario/cadastro.html', context={
        'name': 'funcionario_cadastro'
        }
    )

def lista_clientes(request):
    clientes = Clientes.objects.all()

def lista_produtos(request):
    produtos = Produtos.objects.all()
    produtos_dict = [{'nome': produto.descricao} for produto in produtos]

def cadastrar_fornecedor(request):
    if request.method == 'POST':
        try:
            cliente = cliente_utils.obter_objeto(request)
            validar_cliente.campos_obrigatorios(cliente)
            validar_cliente.campos_unicos(cliente)
            Clientes.objects.create(**cliente)
            return HttpResponse(f'Cliente salvo!\n"{cliente}"')
        except CampoObrigatorioVazio as e:
            return HttpResponseBadRequest(e)
        except CadastroJaExiste as e:
            return HttpResponseBadRequest(e)
        
        def cadastrar_cliente(request):
        if request.method == 'POST':
        try:
            cliente = cliente_utils.obter_objeto(request)
            validar_cliente.campos_obrigatorios(cliente)
            validar_cliente.campos_unicos(cliente)
            Clientes.objects.create(**cliente)
            return HttpResponse(f'Cliente salvo!\n"{cliente}"')
        except CampoObrigatorioVazio as e:
            return HttpResponseBadRequest(e)
        except CadastroJaExiste as e:
            return HttpResponseBadRequest(e)