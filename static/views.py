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

def cliente_cadastro(request):
    cliente = request.POST.get('cliente_cadastro')
    Clientes.objects.create(cliente)
    