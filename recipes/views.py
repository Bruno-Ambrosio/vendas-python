from django.shortcuts import render


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
