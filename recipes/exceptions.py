class CampoObrigatorioVazio(Exception):
    def __init__(self, campo):
        self.campo = campo
        super().__init__(f'Campo obrigatório "{campo}" está vazio!')

class CadastroJaExiste(Exception):
    def __init__(self, campo):
        self.campo = campo
        super().__init__(f'Campo único "{campo}" já cadastrado no banco!')