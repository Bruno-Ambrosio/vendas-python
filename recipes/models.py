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
    fornecedor_nome = models.CharField(max_length=100, null=False, default="")
    fornecedor_cnpj = models.CharField(max_length=20, null=False, unique=True, default="")
    fornecedor_email = models.CharField(max_length=200, unique=True, default="")
    fornecedor_contato = models.CharField(max_length=30)
    fornecedor_cep = models.CharField(max_length=100)
    fornecedor_endereco = models.CharField(max_length=255)
    fornecedor_numero = models.IntegerField()
    fornecedor_complemento = models.CharField(max_length=200)
    fornecedor_bairro = models.CharField(max_length=100)
    fornecedor_cidade = models.CharField(max_length=100)
    fornecedor_estado = models.CharField(max_length=2)
    
    class Meta:
        db_table = 'tb_fornecedores'
    
class Funcionarios(models.Model):
    fornecedor_nome = models.CharField(max_length=100, null=False, default="")
    fornecedor_rg = models.CharField(max_length=30, null=False, unique=True, default="")
    fornecedor_cpf = models.CharField(max_length=20, null=False, unique=True, default="")
    fornecedor_email = models.CharField(max_length=200, null=False, unique=True, default="")
    fornecedor_senha = models.CharField(max_length=10, null=False)
    fornecedor_cargo = models.CharField(max_length=100, null=False)
    fornecedor_nivel_acesso = models.CharField(max_length=50)
    fornecedor_contato = models.CharField(max_length=30)
    fornecedor_cep = models.CharField(max_length=100)
    fornecedor_endereco = models.CharField(max_length=255)
    fornecedor_numero = models.IntegerField()
    fornecedor_complemento = models.CharField(max_length=200)
    fornecedor_bairro = models.CharField(max_length=100)
    fornecedor_cidade = models.CharField(max_length=100)
    fornecedor_estado = models.CharField(max_length=2)
    
    class Meta:
        db_table = 'tb_funcionarios'
    
class Produtos(models.Model):
    fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE, default=1)
    produto_descricao = models.CharField(max_length=100, null=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    qtd_estoque = models.IntegerField(null=False)
    
    class Meta:
        db_table = 'tb_produtos'
    
class Vendas(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    venda_data_venda = models.DateTimeField(null=False)
    venda_total_venda = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    venda_observacoes = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'tb_vendas'
        
class Itens(models.Model):
    venda = models.ForeignKey(Vendas, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    qtd = models.IntegerField(default=1, null=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    
    class Meta:
        db_table = 'tb_itens'