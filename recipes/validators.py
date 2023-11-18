from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from validate_docbr import CPF, CNPJ

def senha_forte(campo):
    if len(campo) < 8:
        raise ValidationError('A senha deve conter no mínimo 8 caracteres!')
    
def em_uso(campo):
    if User.objects.filter(campo=campo).exists():
        raise ValidationError('Usuário já está sendo usado.')
    
def cpf_invalido(campo):
    valida_cpf = CPF()
    return valida_cpf.validate(campo)

def cnpj_invalido(campo):
    valida_cnpj = CNPJ()
    return valida_cnpj.validate(campo)