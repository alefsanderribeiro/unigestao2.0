from django.db import models

class Sexo(models.Model):
    descricao = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Sexo'
        verbose_name_plural = 'Sexo'

    def __str__(self):
        return self.descricao


class Raca(models.Model):
    descricao = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Raça'
        verbose_name_plural = 'Raça'
        
    def __str__(self):
        return self.descricao


class EstadoCivil(models.Model):
    descricao = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estado Civil'
        
    def __str__(self):
        return self.descricao


class GrauInstrucao(models.Model):
    descricao = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Grau de Instrução'
        verbose_name_plural = 'Grau de Instrução'
        
    def __str__(self):
        return self.descricao


class Deficiencia(models.Model):
    descricao = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Deficiencia'
        verbose_name_plural = 'Deficiencia'
        
    def __str__(self):
        return self.descricao


class Nacionalidade(models.Model):
    descricao = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Nacionalidade'
        verbose_name_plural = 'Nacionalidade'
        
    def __str__(self):
        return self.descricao


class UF(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'UF'
        verbose_name_plural = 'UF'
        
    def __str__(self):
        return self.sigla


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        
    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    # Dados Pessoais
    nome_completo = models.CharField(max_length=100)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    grau_instruacao = models.ForeignKey(GrauInstrucao, on_delete=models.CASCADE)
    deficiencia = models.ForeignKey(Deficiencia, on_delete=models.CASCADE, null=True, blank=True)
    nacionalidade = models.ForeignKey(Nacionalidade, on_delete=models.CASCADE)
    nome_mae = models.CharField(max_length=100)
    nome_pai = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True, verbose_name='Ativo')

    # Naturalidade
    naturalidade_uf = models.ForeignKey(UF, related_name='naturalidade', on_delete=models.CASCADE)
    naturalidade_cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name='naturalidade')

    # Documentos
    cpf = models.CharField(max_length=11, unique=True)
    pis_nis = models.CharField(max_length=11, unique=True)
    certificado_militar = models.CharField(max_length=20, null=True, blank=True)
    numero_identidade = models.CharField(max_length=20)
    data_emissao_identidade = models.DateField()
    orgao_expedidor_identidade = models.CharField(max_length=50)
    uf_identidade = models.ForeignKey(UF, related_name='identidade', on_delete=models.CASCADE)

    # Carteira de Trabalho
    numero_ctps = models.CharField(max_length=20)
    serie_ctps = models.CharField(max_length=10)
    data_emissao_ctps = models.DateField()
    uf_ctps = models.ForeignKey(UF, related_name='ctps', on_delete=models.CASCADE)

    # Dados complementares
    cep = models.CharField(max_length=10)
    endereco_uf = models.ForeignKey(UF, related_name='endereco', on_delete=models.CASCADE)
    endereco_cidade = models.ForeignKey(Cidade, related_name='endereco', on_delete=models.CASCADE)
    bairro = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, null=True, blank=True)

    contato = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome_completo
