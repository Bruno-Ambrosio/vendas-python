from django.shortcuts import render, redirect
from .forms import ClienteForms, FornecedorForms, FuncionarioForms
from .models import Clientes, Fornecedores, Funcionarios

cliente_form = ClienteForms()
fornecedor_form = FornecedorForms()
funcionario_form = FuncionarioForms()


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
    if request.method == "POST":
        form = ClienteForms(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect("/")
        except:
            pass
    else:
        form = ClienteForms()
        return render(
            request, 'recipes/pages/cliente/cadastro.html', context={
            'name': 'cliente_cadastro',
            'form': form
            }
        )
    
def fornecedor_cadastro(request):
    if request.method == "POST":
        form = FornecedorForms(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect("/")
        except:
            pass
    else:
        form = FornecedorForms()
        return render(
            request, 'recipes/pages/fornecedor/cadastro.html', context={
            'name': 'fornecedor_cadastro',
            'form': form
            }
        )

def funcionario_cadastro(request):
    if request.method == "POST":
        form = FuncionarioForms(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect("/")
        except:
            pass
    else:
        form = FuncionarioForms()
        return render(
            request, 'recipes/pages/funcionario/cadastro.html', context={
            'name': 'funcionario_cadastro',
            'form': form
            }
        )
        
def cliente_consulta(request):
    if request.method == "GET":
        try:
            clientes = Clientes.objetcts.values('cliente_nome', 'cliente_email', 'cliente_contato')
        except:
            pass
        return render(
            request, 'recipes/pages/cliente/consulta.html', context={
                'name': 'cliente_consulta',
                'clientes': clientes
            }
        )
    else:
        return redirect("/")
    
def funcionario_consulta(request):
    if request.method == "GET":
        try:
            funcionarios = Funcionarios.objetcts.values('funcionario_nome', 'funcionario_email', 'funcionario_contato')
        except:
            pass
        return render(
            request, 'recipes/pages/funcionario/consulta.html', context={
                'name': 'funcionario_consulta',
                'clientes': funcionarios
            }
        )
    else:
        return redirect("/")
    
def fornecedor_consulta(request):
    if request.method == "GET":
        try:
            fornecedores = Fornecedores.objetcts.values('fornecedor_nome', 'fornecedor_email', 'fornecedor_contato')
        except:
            pass
        return render(
            request, 'recipes/pages/fornecedor/consulta.html', context={
                'name': 'fornecedor_consulta',
                'clientes': fornecedores
            }
        )
    else:
        return redirect("/")