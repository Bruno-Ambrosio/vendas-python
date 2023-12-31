# Generated by Django 4.2.6 on 2023-10-30 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_rename_bairro_fornecedores_fornecedor_bairro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedores',
            name='fornecedor_cnpj',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='fornecedores',
            name='fornecedor_email',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='fornecedores',
            name='fornecedor_nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='fornecedor_cpf',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='fornecedor_email',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='fornecedor_nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='fornecedor_rg',
            field=models.CharField(default='', max_length=30, unique=True),
        ),
    ]
