from django import forms
from .models import Clientes, Fornecedores, Funcionarios
from django.contrib.auth.models import User
from .validators import senha_forte, usuario_em_uso, user_email_em_uso, cliente_email_em_uso, fornecedor_email_em_uso, funcionario_email_em_uso, cpf_invalido, cnpj_invalido, contem_numero

class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
    first_name = forms.CharField(label='Nome', validators=[contem_numero])
    last_name = forms.CharField(label='Sobrenome', validators=[contem_numero])
    email = forms.CharField(label='Email', validators=[user_email_em_uso])
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, validators=[senha_forte])

class LoginForms(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, validators=[senha_forte])
        
class ClienteForms(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"
    nome = forms.CharField(label='Nome', validators=[contem_numero])
    rg = forms.CharField(label='RG')
    cpf = forms.CharField(label='CPF', validators=[cpf_invalido])
    email = forms.CharField(label='Email', validators=[cliente_email_em_uso])
        
class FornecedorForms(forms.ModelForm):
    class Meta:
        model = Fornecedores
        fields = "__all__"
    nome = forms.CharField(label='Nome', validators=[contem_numero])
    cnpj = forms.CharField(label='CNPJ', validators=[cnpj_invalido])
    email = forms.CharField(label='Email', validators=[fornecedor_email_em_uso])
        
class FuncionarioForms(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = "__all__"
    nome = forms.CharField(label='Nome', validators=[contem_numero])
    rg = forms.CharField(label='RG')
    cpf = forms.CharField(label='CPF', validators=[cpf_invalido])
    email = forms.CharField(label='Email', validators=[funcionario_email_em_uso])