from django import forms
from .models import Clientes, Fornecedores, Funcionarios
from django.contrib.auth.models import User

class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        labels = {
            'username': 'Usuário',
            'password': 'Senha',
            'email': 'Email',
            'first_name': 'Nome',
            'last_name': 'Sobrenome'
        }

class LoginForms(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
        
class ClienteForms(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"
        labels = {
            'nome': '*Nome',
            'rg': '*RG',
            'cpf': '*CPF',
            'email': '*E-mail'
        }
        
class FornecedorForms(forms.ModelForm):
    class Meta:
        model = Fornecedores
        fields = "__all__"
        labels = {
            'nome': '*Nome',
            'cnpj': '*CNPJ',
            'email': '*E-mail'
        }
        
class FuncionarioForms(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = "__all__"
        labels = {
            'nome': '*Nome',
            'rg': '*RG',
            'cpf': '*CPF',
            'email': '*E-mail'
        }


