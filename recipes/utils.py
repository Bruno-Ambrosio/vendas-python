from django.contrib.auth.hashers import make_password

class ClienteUtils():

    def __init__(self):
        self.cliente = {}
        self.cliente_campos = ['cliente_nome', 'cliente_rg', 'cliente_cpf', 'cliente_email',  'cliente_contato', 'cliente_cep', 'cliente_endereco', 'cliente_numero', 'cliente_complemento', 'cliente_bairro', 'cliente_cidade', 'cliente_estado']

    def obter_objeto(self, request):

        # Percorrendo a lista de campos do objeto inserindo o valor no dicionário do objeto
        for campo in self.cliente_campos:
            self.cliente[campo] = request.POST.get(campo, '')
                
        return self.cliente