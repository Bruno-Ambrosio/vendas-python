from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Produtos, Clientes, Fornecedores
from .exceptions import CampoObrigatorioVazio, CadastroJaExiste
from .validations import ValidarCliente
from .utils import ClienteUtils, FornecedorUtils

fornecedor_utils = FornecedorUtils()
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
    if request.method == 'POST':
        try:
            cliente = cliente_utils.obter_cliente(request)
            validar_cliente.campos_obrigatorios(cliente)
            validar_cliente.campos_unicos(cliente)
            Clientes.objects.create(**cliente)
            return HttpResponse(f'Cliente salvo!\n"{cliente}"')
        except CampoObrigatorioVazio as e:
            return HttpResponseBadRequest(e)
        except CadastroJaExiste as e:
            return HttpResponseBadRequest(e)
    return render(
        request, 'recipes/pages/cliente/cadastro.html', context={
        'name': 'cliente_cadastro'
        }
    )
    
def fornecedor_cadastro(request):
    if request.method == 'POST':
        try:
            fornecedor = fornecedor_utils.obter_fornecedor(request)
            Fornecedores.objects.create(**fornecedor)
            return HttpResponse(f'Fornecedor!\n"{fornecedor}"')
        except CampoObrigatorioVazio as e:
            return HttpResponseBadRequest(e)
        except CadastroJaExiste as e:
            return HttpResponseBadRequest(e) 
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


