from django import forms
from django.contrib.auth.models import User
from .models import Clientes, Fornecedores, Funcionarios
from validate_docbr import CPF, CNPJ
import re

cpf = CPF()
cnpj = CNPJ()

def rg_valido(value):
    if len(value) != 10:
        raise forms.ValidationError('RG informado é inválido!')

def cpf_valido(value):
    if not cpf.validate(value):
        raise forms.ValidationError('CPF informado é inválido!')
    
def cnpj_valido(value):
    if not cnpj.validate(value):
        raise forms.ValidationError('CNPJ informado é inválido!')

def senha_forte(value):
    if len(value) < 8:
        raise forms.ValidationError('A senha deve conter no mínimo 8 caracteres!')
    
def usuario_em_uso(value):
    if User.objects.filter(username=value).exists():
        raise forms.ValidationError('Usuário já está sendo usado.')

def user_email_em_uso(value):
    if User.objects.filter(email=value).exists():
        raise forms.ValidationError('Usuário já está sendo usado.')
    
def cliente_email_em_uso(value):
    if Clientes.objects.filter(email=value).exists():
        raise forms.ValidationError('Usuário já está sendo usado.')
    
def fornecedor_email_em_uso(value):
    if Fornecedores.objects.filter(email=value).exists():
        raise forms.ValidationError('Usuário já está sendo usado.')
    
def funcionario_email_em_uso(value):
    if Funcionarios.objects.filter(email=value).exists():
        raise forms.ValidationError('Usuário já está sendo usado.')

def contem_numero(value):
    if re.search(r'\d', value):
        raise forms.ValidationError(f'O campo "{value}" não deve conter números.')