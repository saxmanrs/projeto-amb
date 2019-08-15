from django.db import models

# Create your models here.

class CboModel(models.Model):
    nome_cbo = models.CharField('Profissão', max_length=50)

    def __str__(self):
        return self.nome_cbo


class PessoaModel (models.Model):
    TIPO_PESSOA =  (
        ("MENOR","menor"),
        ("MAIOR","maior"),
    )
    tp_pessoa = models.CharField('Tipo de Pessoa', max_length=30, choices=TIPO_PESSOA)
    nome_pessoa = models.CharField('Nome ', max_length=50)
    fone_pessoa = models.CharField('Telefone ', max_length=30)
    cpf_pessoa = models.CharField('CPF', max_length=11)
    rg_pessoa = models.CharField('RG', max_length=15)
    profissao_cbo = models.ForeignKey(CboModel,null=True,blank=True,on_delete=models.CASCADE)
    ESTADOCIVIL_PESSOA = (
        ("CASADO","casado"),
        ("SOLTEIRO","solteiro"),
        ("DIVORCIADO","divorciado"),
        ("VIUVO","viuvo"),
        ("UNIÃO ESTAVEL","uniao_estavel"),
        
    )
    estCivil_pessoa = models.CharField('Estado Civil',max_length=30, choices=ESTADOCIVIL_PESSOA)
    endereco_pessoa =models.CharField('Endereço', max_length=40)
    cep_pessoa = models.CharField('CEP', max_length=8)
    bairro_pessoa = models.CharField('Bairro', max_length=40)
    bairro_pessoa = models.CharField('Municipio', max_length=50)
    UF =(
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )

    uf_pessoa = models.CharField('Estado', max_length=30,choices=UF)



    def __str__(self):
        return self.nome_pessoa



