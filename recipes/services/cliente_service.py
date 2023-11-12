from django.contrib.auth.hashers import make_password

class ClienteService():

    def __init__(self):
        self.cliente = {}
        self.cliente_campos = ['nome', 'rg', 'cpf', 'email', 'telefone', 'celular', 'cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'estado']

    def obter_objeto(self, request):

        # Percorrendo a lista de campos do objeto inserindo o valor no dicionário do objeto
        for campo in self.cliente_campos:
            self.cliente[campo] = request.POST.get(campo, '')
                
        return self.cliente