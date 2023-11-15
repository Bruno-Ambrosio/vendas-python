from django.contrib import admin
from .models import Clientes, Funcionarios, Fornecedores

# Register your models here.
admin.site.register(Clientes)
admin.site.register(Funcionarios)
admin.site.register(Fornecedores)