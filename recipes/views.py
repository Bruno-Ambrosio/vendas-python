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
            user = authenticate(request, username=usuario, password=senha)
            if user is not None:
                print('aqui')
                login_django(request, user)
                messages.success(request, 'Logado com sucesso!')
                return redirect('/')
            else:
                messages.warning(request, 'Usuário ou senha inválido(s)!')
                return redirect(request.path)
    else:
        form = LoginForms()
    print(form.errors)
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
    form = FuncionarioForms()
    return render(
        request, 'recipes/pages/funcionario/cadastro.html', context={
        'name': 'funcionario_cadastro',
        'form': form
        }
    )
        
def cliente_consulta(request):
    if request.method == "GET":
        clientes = Clientes.objects.all()
        return render(
            request, 'recipes/pages/cliente/consulta.html', context={
                'name': 'cliente_consulta',
                'clientes': clientes
            }
        )
    
def funcionario_consulta(request):
    if request.method == "GET":
        funcionarios = Funcionarios.objects.all()
        return render(
            request, 'recipes/pages/funcionario/consulta.html', context={
                'name': 'funcionario_consulta',
                'clientes': funcionarios
            }
        )
    
def fornecedor_consulta(request):
    if request.method == "GET":
        fornecedores = Fornecedores.objects.all()
        return render(
            request, 'recipes/pages/fornecedor/consulta.html', context={
                'name': 'fornecedor_consulta',
                'clientes': fornecedores
            }
        )