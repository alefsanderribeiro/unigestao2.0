from django.db import models


class CBO(models.Model):
    code = models.CharField(max_length=10, unique=True, verbose_name='Código CBO')
    occupation = models.CharField(max_length=200, verbose_name='Ocupação')

    def __str__(self):
        return f'{self.code} - {self.occupation}'

    class Meta:
        verbose_name = 'CBO'
        verbose_name_plural = 'CBOs'


class Occupation(models.Model):
    cbo = models.ForeignKey(CBO, related_name='occupations', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Nome da Ocupação')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ocupação'
        verbose_name_plural = 'Ocupações'


class Synonym(models.Model):
    occupation = models.ForeignKey(Occupation, related_name='synonyms', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='Sinônimo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sinônimo'
        verbose_name_plural = 'Sinônimos'
