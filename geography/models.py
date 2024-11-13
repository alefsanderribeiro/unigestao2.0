from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nome do País')

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do Estado')
    abbreviation = models.CharField(max_length=2, unique=True, verbose_name='Sigla')
    code = models.CharField(max_length=3, verbose_name='Código')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="states", verbose_name='País')

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return f'{self.abbreviation} - {self.name}'


class Capital(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome da Capital')
    state = models.OneToOneField(State, on_delete=models.CASCADE, related_name="capital", verbose_name='Estado')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="capitals", verbose_name='País')

    class Meta:
        verbose_name = 'Capital'
        verbose_name_plural = 'Capitais'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome da Cidade')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="cities", verbose_name='Estado')

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return f'{self.name} - {self.state}'


class Region(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome da Região')
    states = models.ManyToManyField(State, related_name="regions", verbose_name='Estados')

    class Meta:
        verbose_name = 'Região'
        verbose_name_plural = 'Regiões'

    def __str__(self):
        return self.name
