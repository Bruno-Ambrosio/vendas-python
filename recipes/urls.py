
from django.urls import include, path

from recipes.views import home, login, cliente_cadastro


urlpatterns = [
    path('login', login),
    path('home', home),
    path('cliente/cadastro', cliente_cadastro)
]