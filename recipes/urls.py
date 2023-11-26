
from django.urls import path
from recipes.views import home, login, sair, cliente_editar, fornecedor_editar, funcionario_editar, cliente_cadastro, funcionario_cadastro, funcionario_consulta, fornecedor_cadastro, usuario_cadastro, cliente_consulta, fornecedor_consulta

urlpatterns = [
    path('', login, name='login'),
    path('sair', sair, name='sair'),
    path('usuario/cadastro', usuario_cadastro, name='usuario_cadastro'),
    path('home', home, name='home'),
    path('cliente/cadastro', cliente_cadastro, name='cliente_cadastro'),
    path('funcionario/cadastro', funcionario_cadastro, name='funcionario_cadastro'),
    path('fornecedor/cadastro', fornecedor_cadastro, name='fornecedor_cadastro'),
    path('cliente/consulta', cliente_consulta, name='cliente_consulta'),
    path('fornecedor/consulta', fornecedor_consulta, name='fornecedor_consulta'),
    path('funcionario/consulta', funcionario_consulta, name='funcionario_consulta'),
    path('cliente/editar/<int:id>/', cliente_editar, name='cliente_editar'),
    path('fornecedor/editar/<int:id>/', fornecedor_editar, name='fornecedor_editar'),
    path('funcionario/editar/<int:id>/', funcionario_editar, name='funcionario_editar')

]