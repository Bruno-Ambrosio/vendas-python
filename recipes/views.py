from django.shortcuts import render
from django.http import JsonResponse
from .models import Produtos, Clientes

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
    return JsonResponse(f'Lista de pessoas: {clientes}')

def lista_produtos(request):
    produtos = Produtos.objects.all()
    produtos_dict = [{'nome': produto.descricao} for produto in produtos]
    return JsonResponse(f'Lista de produtos: {produtos_dict}', safe=False)

def cadastrar_cliente(request):
    if request.method == 'POST':
        cliente_dict = cliente_map(request)
        Clientes.objects.create(cliente_dict)

def cliente_map(request):

    campos_vazios = []

    for campo, valor in request.POST.items():
        if valor == '':
            campos_vazios.append(campo)

    cliente = {
        'nome': request.POST['nome'],
        'rg': request.POST['rg'],
        'cpf': request.POST['cpf'],
        'email': request.POST['email'],
        'telefone': request.POST['telefone'],
        'celular': request.POST['celular'],
        'cep': request.POST['cep'],
        'endereco': request.POST['endereco'],
        'numero': request.POST['numero'],
        'complemento': request.POST['complemento'],
        'bairro': request.POST['bairro'],
        'cidade': request.POST['cidade'],
        'estado': request.POST['estado']
    }

    return cliente