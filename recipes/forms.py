from django import forms
from .models import Clientes, Fornecedores, Funcionarios

class ClienteForms(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"

class FornecedorForms(forms.ModelForm):
    class Meta:
        model = Fornecedores
        fields = "__all__"
        
class FuncionarioForms(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = "__all__"


