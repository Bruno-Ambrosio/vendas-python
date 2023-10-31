# Generated by Django 4.2.6 on 2023-10-31 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_alter_fornecedores_fornecedor_cnpj_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fornecedores',
            old_name='fornecedor_celular',
            new_name='fornecedor_contato',
        ),
        migrations.RenameField(
            model_name='funcionarios',
            old_name='fornecedor_celular',
            new_name='fornecedor_contato',
        ),
        migrations.RenameField(
            model_name='vendas',
            old_name='venda_data_venda',
            new_name='data_venda',
        ),
        migrations.RenameField(
            model_name='vendas',
            old_name='venda_observacoes',
            new_name='observacoes',
        ),
        migrations.RenameField(
            model_name='vendas',
            old_name='venda_total_venda',
            new_name='total_venda',
        ),
        migrations.RemoveField(
            model_name='fornecedores',
            name='fornecedor_telefone',
        ),
        migrations.RemoveField(
            model_name='funcionarios',
            name='fornecedor_telefone',
        ),
    ]