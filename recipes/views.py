from django.shortcuts import render, redirect
from .forms import ClienteForms, FornecedorForms, FuncionarioForms, UserForms, LoginForms
from .models import Clientes, Fornecedores, Funcionarios
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'home'
    })

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            senha = form.cleaned_data['password']
            user = authenticate(username=usuario, password=senha)
            if user is not None:
                login_django(request, user)
                messages.success(request, 'Logado com sucesso!')
                return redirect(request.path)
            else:
                messages.warning(request, 'Usuário ou senha inválido(s)!')
                return redirect(request.path)
    else:
        form = LoginForms()
        return render(
            request, 'recipes/pages/login.html', context={
            'name': 'login',
            'form': form,
            }
    )

def usuario_cadastro(request):
    if request.method == "POST":
        form = UserForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("/")
    form = UserForms()
    return render(
        request, 'recipes/pages/usuario/cadastro.html', context={
        'name': 'usuario_cadastro',
        'form': form
        }
    )

def cliente_cadastro(request):
    if request.method == "POST":
        form = ClienteForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('')
        else:
            for field in form.errors.items():
                messages.warning(request, f'Campo inválido: "{field}"')
                return redirect(request.path)
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
        if form.is_valid():
            form.save()
            return redirect("/")
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
        if form.is_valid():
            form.save()
            return redirect("/")
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
        clientes = Clientes.objetcts.values('nome', 'email', 'contato')
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
        funcionarios = Funcionarios.objetcts.values('nome', 'email', 'contato')
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
        fornecedores = Fornecedores.objetcts.values('nome', 'email', 'contato')
        return render(
            request, 'recipes/pages/fornecedor/consulta.html', context={
                'name': 'fornecedor_consulta',
                'clientes': fornecedores
            }
        )
    else:
        return redirect("/")