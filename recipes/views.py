from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'home'
    })

def login(request):
    return render(
        request, 'recipes/pages/login.html', context={
        'name': 'login'
        }
    )

def menu(request):
    return render(
        request, 'recipes/pages/menu.html', context={
        'name': 'menu'
        }
    )
