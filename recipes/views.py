from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .forms import ClienteForms, FornecedorForms, FuncionarioForms, UserForms, LoginForms, ClienteEdtForms, FuncionarioEdtForms, FornecedorEdtForms
from .models import Clientes, Fornecedores, Funcionarios
from django.contrib.auth import authenticate, login as login_django, logout
from django.contrib.auth.decorators import login_required
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
                form.add_error(None, 'Usuário ou senha inválido(s)')
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

def usuario_cadastro(request):
    if request.method == "POST":
        form = UserForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('/')
    else:
        form = UserForms()
    
    if not request.user.is_authenticated:
        return render(
            request, 'recipes/pages/usuario/cadastro.html', context={
            'name': 'usuario_cadastro',
            'form': form
            }
        )
    else:
        return redirect('/home')

@login_required()
def sair(request):
    if request.method == 'POST':
        messages.success(request, 'Sessão encerrada.')
        logout(request)
        return redirect('/')

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
            messages.success(request, 'Fornecedor cadastrado com sucesso!')
            return redirect("/fornecedor/consulta")
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
            messages.success(request, 'Funcionário cadastrado com sucesso!')
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
                'funcionarios': funcionarios
            }
        )

@login_required() 
def fornecedor_consulta(request):
    if request.method == "GET":
        fornecedores = Fornecedores.objects.all()
        return render(
            request, 'recipes/pages/fornecedor/consulta.html', context={
                'name': 'fornecedor_consulta',
                'fornecedores': fornecedores
            }
        )

@login_required() 
def funcionario_editar(request, id):
    funcionario = get_object_or_404(Funcionarios, pk=id)
    if request.method == 'POST':
        form = FuncionarioEdtForms(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário editado com sucesso!')
            return redirect('/funcionario/consulta')
    else:
        form = FuncionarioEdtForms(instance=funcionario)
    return render(
        request, 'recipes/pages/funcionario/editar.html', context={
            'name': 'editar_funcionario',
            'form': form,
            'funcionario': funcionario
        }
    )
 
@login_required()    
def cliente_editar(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    if request.method == 'POST':
        form = ClienteEdtForms(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente editado com sucesso!')
            return redirect('/cliente/consulta')
    else:
        form = ClienteEdtForms(instance=cliente)
    return render(
        request, 'recipes/pages/cliente/editar.html', context={
            'name': 'editar_cliente',
            'form': form,
            'cliente': cliente
        }
    )
    
@login_required()    
def fornecedor_editar(request, id):
    fornecedor = get_object_or_404(Fornecedores, pk=id)
    if request.method == 'POST':
        form = FornecedorEdtForms(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fornecedor editado com sucesso!')
            return redirect('/fornecedor/consulta')
    else:
        form = FornecedorEdtForms(instance=fornecedor)
    return render(
        request, 'recipes/pages/fornecedor/editar.html', context={
            'name': 'editar_fornecedor',
            'form': form,
            'fornecedor': fornecedor
        }
    )

@login_required() 
def cliente_excluir(request, id):
    cliente = get_object_or_404(Clientes, pk=id)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
        return redirect('/cliente/consulta')

@login_required() 
def funcionario_excluir(request, id):
    funcionario = get_object_or_404(Funcionarios, pk=id)
    if request.method == 'POST':
        funcionario.delete()
        messages.success(request, 'Funcionário excluído com sucesso!')
        return redirect('/funcionario/consulta')

@login_required()   
def fornecedor_excluir(request, id):
    fornecedor = get_object_or_404(Fornecedores, pk=id)
    if request.method == 'POST':
        fornecedor.delete()
        messages.success(request, 'Fornecedor excluído com sucesso!')
        return redirect('/fornecedor/consulta')