
from django.urls import include, path
from recipes.views import home, login, cliente_cadastro, funcionario_cadastro, fornecedor_cadastro
from recipes.views import home, login, lista_produtos, cadastrar_cliente

urlpatterns = [
    path('login', login),
    path('home', home),
    path('cliente/cadastro', cliente_cadastro),
    path('funcionario/cadastro', funcionario_cadastro),
    path('fornecedor/cadastro', fornecedor_cadastro),
    path('produtos', lista_produtos, name='lista_produtos'),
    path('cadastrar_cliente', cadastrar_cliente, name='cadastrar_cliente')
]