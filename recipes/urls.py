
from django.urls import path
from recipes.views import home, login, cliente_cadastro, funcionario_cadastro, fornecedor_cadastro
from recipes.views import home, login

urlpatterns = [
    path('login', login),
    path('home', home),
    path('cliente/cadastro', cliente_cadastro, name='cliente_cadastro'),
    path('funcionario/cadastro', funcionario_cadastro),
    path('fornecedor/cadastro', fornecedor_cadastro),
]