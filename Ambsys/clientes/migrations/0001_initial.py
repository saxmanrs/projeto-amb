# Generated by Django 2.2.2 on 2019-08-15 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CboModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cbo', models.CharField(max_length=50, verbose_name='Profissão')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tp_pessoa', models.CharField(choices=[('MENOR', 'menor'), ('MAIOR', 'maior')], max_length=30, verbose_name='Tipo de Pessoa')),
                ('nome_pessoa', models.CharField(max_length=50, verbose_name='Nome ')),
                ('fone_pessoa', models.CharField(max_length=30, verbose_name='Telefone ')),
                ('cpf_pessoa', models.CharField(max_length=11, verbose_name='CPF')),
                ('rg_pessoa', models.CharField(max_length=15, verbose_name='RG')),
                ('estCivil_pessoa', models.CharField(choices=[('CASADO', 'casado'), ('SOLTEIRO', 'solteiro'), ('DIVORCIADO', 'divorciado'), ('VIUVO', 'viuvo'), ('UNIÃO ESTAVEL', 'uniao_estavel')], max_length=30, verbose_name='Estado Civil')),
                ('endereco_pessoa', models.CharField(max_length=40, verbose_name='Endereço')),
                ('cep_pessoa', models.CharField(max_length=8, verbose_name='CEP')),
                ('bairro_pessoa', models.CharField(max_length=50, verbose_name='Municipio')),
                ('uf_pessoa', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=30, verbose_name='Estado')),
                ('profissao_cbo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.CboModel')),
            ],
        ),
    ]
