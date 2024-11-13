from django.db import models

class Gender(models.Model):
    description = models.CharField(max_length=20, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        return self.description


class Race(models.Model):
    description = models.CharField(max_length=30, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Raça'
        verbose_name_plural = 'Raça'
        
    def __str__(self):
        return self.description


class MaritalStatus(models.Model):
    description = models.CharField(max_length=20, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Estado Civil'
        verbose_name_plural = 'Estado Civil'
        
    def __str__(self):
        return self.description


class DegreeInstruction(models.Model):
    description = models.CharField(max_length=30, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Grau de Instrução'
        verbose_name_plural = 'Grau de Instrução'
        
    def __str__(self):
        return self.description


class Deficiency(models.Model):
    description = models.CharField(max_length=50, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Deficiência'
        verbose_name_plural = 'Deficiência'
        
    def __str__(self):
        return self.description


class Nationality(models.Model):
    description = models.CharField(max_length=50, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Nacionalidade'
        verbose_name_plural = 'Nacionalidade'
        
    def __str__(self):
        return self.description


class AdmissionType(models.Model):
    description = models.CharField(max_length=100, verbose_name='Descrição')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Tipo de Admissão'
        verbose_name_plural = 'Tipos de Admissão'


class HarmfulExposure(models.Model):
    description = models.CharField(max_length=100, verbose_name='Descrição')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Exposição a Agentes Nocivos'
        verbose_name_plural = 'Exposições a Agentes Nocivos'


class PaymentType(models.Model):
    description = models.CharField(max_length=100, verbose_name='Descrição')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Tipo de Pagamento'
        verbose_name_plural = 'Tipos de Pagamento'


class Bank(models.Model):
    description = models.CharField(max_length=100, verbose_name='Descrição')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'


class AccountType(models.Model):
    description = models.CharField(max_length=100, verbose_name='Descrição')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Tipo de Conta'
        verbose_name_plural = 'Tipos de Conta'


class PixType(models.Model):
    description = models.CharField(max_length=100, verbose_name='Descrição')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Tipo de Pix'
        verbose_name_plural = 'Tipos de Pix'
