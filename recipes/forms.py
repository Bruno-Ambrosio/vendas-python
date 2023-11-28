from django import forms
from .models import Clientes, Fornecedores, Funcionarios
from django.contrib.auth.models import User
from .validators import senha_forte, cpf_valido, cnpj_valido, rg_valido, usuario_em_uso, user_email_em_uso, cliente_email_em_uso, fornecedor_email_em_uso, funcionario_email_em_uso, contem_numero

class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
    first_name = forms.CharField(label='Nome', validators=[contem_numero])
    last_name = forms.CharField(label='Sobrenome', validators=[contem_numero])
    email = forms.EmailField(label='Email', validators=[user_email_em_uso])
    username = forms.CharField(label='Usuário', validators=[usuario_em_uso])
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, validators=[senha_forte])

class LoginForms(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    
class ClienteEdtForms(forms.ModelForm):
    class Meta:
        model = Clientes
        exclude = ['cpf', 'rg']
    nome = forms.CharField(label='Nome', validators=[contem_numero])
    email = forms.EmailField(label='Email')
    
        
class ClienteForms(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"
    nome = forms.CharField(label='Nome', validators=[contem_numero])
    rg = forms.CharField(label='RG', validators=[rg_valido])
    cpf = forms.CharField(label='CPF', validators=[cpf_valido])
    email = forms.EmailField(label='Email', validators=[cliente_email_em_uso])
    
class FornecedorEdtForms(forms.ModelForm):
    class Meta:
        model = Fornecedores
        exclude = ['cnpj']
    nome = forms.CharField(label='Nome', validators=[contem_numero])
    email = forms.EmailField(label='Email')
        
class FornecedorForms(forms.ModelForm):
    class Meta:
        model = Fornecedores
        fields = "__all__"
    nome = forms.CharField(label='Nome', validators=[contem_numero])
    cnpj = forms.CharField(label='CNPJ', validators=[cnpj_valido])
    email = forms.EmailField(label='Email', validators=[fornecedor_email_em_uso])

class FuncionarioEdtForms(forms.ModelForm):
    class Meta:
        model = Funcionarios
        exclude = ['cpf', 'rg']
    nome = forms.CharField(label='Nome', validators=[contem_numero])
    email = forms.EmailField(label='Email')
    
class FuncionarioForms(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = "__all__"
    nome = forms.CharField(label='Nome', validators=[contem_numero])
    rg = forms.CharField(label='RG', validators=[rg_valido])
    cpf = forms.CharField(label='CPF', validators=[cpf_valido])
    email = forms.EmailField(label='Email', validators=[funcionario_email_em_uso])