
from django.urls import include, path

from recipes.views import home, login, cliente_cadastro, funcionario_cadastro, fornecedor_cadastro


urlpatterns = [
    path('login', login),
    path('home', home),
    path('cliente/cadastro', cliente_cadastro),
    path('funcionario/cadastro', funcionario_cadastro),
    path('fornecedor/cadastro', fornecedor_cadastro),

]