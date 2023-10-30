from django.db import models

class Clientes(models.Model):
    cliente_nome = models.CharField(max_length=100, null=False, default="")
    cliente_rg = models.CharField(max_length=30, null=False, unique=True, default="")
    cliente_cpf = models.CharField(max_length=20, null=False, unique=True, default="")
    cliente_email = models.CharField(max_length=200, null=False, unique=True, default="")
    cliente_contato = models.CharField(max_length=30)
    cliente_cep = models.CharField(max_length=100)
    cliente_endereco = models.CharField(max_length=255)
    cliente_numero = models.IntegerField()
    cliente_complemento = models.CharField(max_length=200)
    cliente_bairro = models.CharField(max_length=100)
    cliente_cidade = models.CharField(max_length=100)
    cliente_estado = models.CharField(max_length=2)
    
    class Meta:
        db_table = 'tb_clientes'
    
class Fornecedores(models.Model):
    nome = models.CharField(max_length=100, null=False)
    cnpj = models.CharField(max_length=20, null=False, unique=True)
    email = models.CharField(max_length=200, unique=True)
    telefone = models.CharField(max_length=30)
    celular = models.CharField(max_length=30)
    cep = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    
    class Meta:
        db_table = 'tb_fornecedores'
    
class Funcionarios(models.Model):
    nome = models.CharField(max_length=100, null=False)
    rg = models.CharField(max_length=30, null=False, unique=True)
    cpf = models.CharField(max_length=20, null=False, unique=True)
    email = models.CharField(max_length=200, null=False, unique=True)
    senha = models.CharField(max_length=10, null=False)
    cargo = models.CharField(max_length=100, null=False)
    nivel_acesso = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30)
    celular = models.CharField(max_length=30)
    cep = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    
    class Meta:
        db_table = 'tb_funcionarios'
    
class Produtos(models.Model):
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE, default=1)
    descricao = models.CharField(max_length=100, null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    qtd_estoque = models.IntegerField(null=False)
    
    class Meta:
        db_table = 'tb_produtos'
    
class Vendas(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    data_venda = models.DateTimeField(null=False)
    total_venda = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    observacoes = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'tb_vendas'
        
class Itens(models.Model):
    venda = models.ForeignKey(Vendas, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    qtd = models.IntegerField(default=1, null=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    
    class Meta:
        db_table = 'tb_itens'