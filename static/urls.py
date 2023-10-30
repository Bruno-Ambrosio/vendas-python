
from django.urls import include, path

from recipes.views import home, login, menu, lista_produtos

urlpatterns = [
    path('', login),
    path('home', home),
    path('menu', menu),
    path('produtos', lista_produtos, name='lista_produtos'),
]