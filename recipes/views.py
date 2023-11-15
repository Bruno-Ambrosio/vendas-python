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
        try:
            if form.is_valid():
                usuario = form.cleaned_data['username']
                senha = form.cleaned_data['password']
                print(usuario, ' ', senha)
                user = authenticate(username=usuario, password=senha)
                print(user)
                if user is not None:
                    login_django(request, user)
                    messages.success(request, 'Logado com sucesso!')
                    return redirect('/login')
                else:
                    messages.warning(request, 'Usuário ou senha inválido(s)!')
                    return redirect('/login')
            else:
                messages.warning(request, 'Usuário ou senha inválido(s)!')
                return redirect('/login')
        except:
            messages.error(request, 'Ocorreu um erro ao processar o login.')
            return redirect('/login')
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
        try:
            if form.is_valid():
                usuario = form.cleaned_data['username']
                senha = form.cleaned_data['password']
                email = form.cleaned_data['email']
                nome = form.cleaned_data['first_name']
                sobrenome = form.cleaned_data['last_name']
                user = User.objects.create_user(username=usuario, password=senha, email=email, first_name=nome, last_name=sobrenome)
                user.save()
                return redirect("/")
        except:
            pass
    else:
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