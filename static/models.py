from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=30)
    cpf = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
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
        db_table = 'tb_clientes'
    
class Fornecedores(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
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
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=30)
    cpf = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=10)
    cargo = models.CharField(max_length=100)
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
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_estoque = models.IntegerField()
    for_id = models.IntegerField()
    
    class Meta:
        db_table = 'tb_produtos'
    
class Vendas(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    data_venda = models.DateTimeField()
    total_venda = models.DecimalField(max_digits=10, decimal_places=2)
    observacoes = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'tb_vendas'