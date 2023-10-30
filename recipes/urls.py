
from django.urls import include, path

from recipes.views import home, login, menu, lista_produtos, cadastrar_cliente

urlpatterns = [
    path('', login),
    path('home', home),
    path('menu', menu),
    path('produtos', lista_produtos, name='lista_produtos'),
    path('cadastrar_cliente', cadastrar_cliente, name='cadastrar_cliente')
]