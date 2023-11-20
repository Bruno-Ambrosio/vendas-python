
from django.urls import path
from recipes.views import home, login, cliente_cadastro, funcionario_cadastro, fornecedor_cadastro, usuario_cadastro, cliente_consulta

urlpatterns = [
    path('login', login, name='login'),
    path('usuario/cadastro', usuario_cadastro, name='usuario_cadastro'),
    path('home', home, name='home'),
    path('cliente/cadastro', cliente_cadastro, name='cliente_cadastro'),
    path('funcionario/cadastro', funcionario_cadastro, name='funcionario_cadastro'),
    path('fornecedor/cadastro', fornecedor_cadastro, name='fornecedor_cadastro'),
    path('cliente/consulta', cliente_consulta, name='cliente_consulta'),
]