# Generated by Django 4.2.6 on 2023-10-24 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_clientes_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='itens',
            name='qtd',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='fornecedores',
            name='numero',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='numero',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='qtd_estoque',
            field=models.SmallIntegerField(),
        ),
    ]
