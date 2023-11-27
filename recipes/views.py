from django.shortcuts import render, redirect, get_object_or_404

from django.http import JsonResponse
from .forms import ClienteForms, FornecedorForms, FuncionarioForms, UserForms, LoginForms
from .models import Clientes, Fornecedores, Funcionarios
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            senha = form.cleaned_data['password']
            user = authenticate(request, username=usuario, password=senha)
            if user is not None:
                login_django(request, user)
                messages.success(request, 'Logado com sucesso!')
                return redirect('/home')
            else:
                messages.warning(request, 'Usuário ou senha inválido(s)!')
                return redirect(request.path)
    else:
        form = LoginForms()
    if not request.user.is_authenticated:
        return render(
            request, 'recipes/pages/login.html', context={
            'name': 'login',
            'form': form,
            }
        )
    else:
        return redirect('/home')

def sair(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')

def usuario_cadastro(request):
    if request.method == "POST":
        form = UserForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/')
    else:
        form = UserForms()
    
    if request.user.is_authenticated:
        return render(
            request, 'recipes/pages/usuario/cadastro.html', context={
            'name': 'usuario_cadastro',
            'form': form
            }
        )
    else:
        return redirect('/home')

@login_required()
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'home'
    })

@login_required()
def cliente_cadastro(request):
    if request.method == "POST":
        form = ClienteForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('/cliente/consulta')
    else:
        form = ClienteForms()
    return render(
        request, 'recipes/pages/cliente/cadastro.html', context={
        'name': 'cliente_cadastro',
        'form': form
        }
    )

@login_required()
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

@login_required()
def funcionario_cadastro(request):
    if request.method == "POST":
        form = FuncionarioForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/funcionario/consulta")
    else:
        form = FuncionarioForms()
    return render(
        request, 'recipes/pages/funcionario/cadastro.html', context={
        'name': 'funcionario_cadastro',
        'form': form
        }
    )

@login_required()       
def cliente_consulta(request):
    if request.method == "GET":
        clientes = Clientes.objects.all()
        return render(
            request, 'recipes/pages/cliente/consulta.html', context={
                'name': 'cliente_consulta',
                'clientes': clientes
            }
        )

@login_required()
def funcionario_consulta(request):
    if request.method == "GET":
        funcionarios = Funcionarios.objects.all()
        return render(
            request, 'recipes/pages/funcionario/consulta.html', context={
                'name': 'funcionario_consulta',
                'clientes': funcionarios
            }
        )

@login_required() 
def fornecedor_consulta(request):
    if request.method == "GET":
        fornecedores = Fornecedores.objects.all()
        return render(
            request, 'recipes/pages/fornecedor/consulta.html', context={
                'name': 'fornecedor_consulta',
                'clientes': fornecedores
            }
        )

def funcionario_editar(request, id):
    funcionario = get_object_or_404(Funcionarios, pk=id)
    if request.method == 'POST':
        form = FuncionarioForms(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('/funcionario/consulta')
    else:
        form = FuncionarioForms()
    return render(
        request, 'recipes/pages/funcionario/consulta.html', context={
            'name': 'editar_funcionario',
            'form': form
        }
    )
    
def cliente_editar(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    if request.method == 'POST':
        form = ClienteForms(request.POST, instance=cliente)
        print(form)
        if form.is_valid():
            print('aqui')
            form.save()
            return redirect('/cliente/consulta')
    else:
        form = ClienteForms(instance=cliente)
    return render(
        request, 'recipes/pages/cliente/editar.html', context={
            'name': 'editar_funcionario',
            'form': form,
            'cliente': cliente
        }
    )
    
def fornecedor_editar(request, id):
    fornecedor = get_object_or_404(Fornecedores, pk=id)
    if request.method == 'POST':
        form = FornecedorForms(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('/fornecedor/consulta')
    else:
        form = FornecedorForms()
    return render(
        request, 'recipes/pages/fornecedor/consulta.html', context={
            'name': 'editar_funcionario',
            'form': form
        }
    )