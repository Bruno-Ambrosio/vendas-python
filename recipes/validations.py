from .models import Clientes
from .exceptions import CampoObrigatorioVazio, CadastroJaExiste

class ValidarCliente():
    
    def campos_obrigatorios(self, cliente):

        # Mapeamento dos campos obrigatórios do objeto
        campos_obrigatorios = ['cliente_nome', 'cliente_rg', 'cliente_cpf', 'cliente_email', 'cliente_contato']

        # Percorrendo a lista de campos vazios, se algum campo obrigatório estiver vazio ele retorna exceção
        for campo in campos_obrigatorios:
            if cliente[campo] == '':
                raise CampoObrigatorioVazio(campo)

        return cliente
            
    def campos_unicos(self, cliente):

        # Mapeamento dos campos únicos do objeto
        campos_unicos = ['cliente_rg', 'cliente_cpf', 'cliente_email', 'cliente_contato']

        # Percorrendo o dicionário do objeto, se houver campos unicos repetidos ele retorna exceção
        for campo in campos_unicos:
            if campo in cliente:
                filtro = {campo: cliente[campo]}
                if Clientes.objects.filter(**filtro).exists():
                    raise CadastroJaExiste(campo)
        
        return cliente