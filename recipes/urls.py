
from django.urls import include, path

from recipes.views import home, login, menu

urlpatterns = [
    path('', login),
    path('home', home),
    path('menu', menu),
]