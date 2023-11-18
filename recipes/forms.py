from django import forms
from .models import Clientes, Fornecedores, Funcionarios
from django.contrib.auth.models import User
from .validators import senha_forte, em_uso, cpf_invalido, cnpj_invalido

class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.CharField(label='Email', validators=[em_uso])
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, validators=[senha_forte])

class LoginForms(forms.Form):
    username = forms.CharField(label='Usuário', validators=[em_uso])
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, validators=[])
        
class ClienteForms(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"
    nome = forms.CharField(label='Nome')
    rg = forms.CharField(label='RG')
    cpf = forms.CharField(label='CPF', validators=[cpf_invalido])
    email = forms.CharField(label='Email', validators=[em_uso])
        
class FornecedorForms(forms.ModelForm):
    class Meta:
        model = Fornecedores
        fields = "__all__"
        labels = {
            'nome': '*Nome',
            'cnpj': '*CNPJ',
            'email': '*E-mail'
        }
    nome = forms.CharField(label='Nome')
    cnpj = forms.CharField(label='CNPJ', validators=[cnpj_invalido])
    email = forms.CharField(label='Email', validators=[em_uso])
        
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


