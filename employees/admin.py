from django.contrib import admin
from . import models

class SexoAdm(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


class RacaAdm(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


class EstadoCivilAdm(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


class GrauInstrucaoAdm(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


class DeficienciaAdm(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


class NacionalidadeAdm(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


class UFAdm(admin.ModelAdmin):
    list_display = ('sigla','nome',)
    search_fields = ('sigla',)


class CidadeAdm(admin.ModelAdmin):
    list_display = ('nome','uf',)
    search_fields = ('nome',)


class FuncionarioAdm(admin.ModelAdmin):
    list_display = ('nome_completo','cpf','telefone')
    search_fields = ('nome_completo',)


admin.site.register(models.Sexo, SexoAdm)
admin.site.register(models.Raca, RacaAdm)
admin.site.register(models.EstadoCivil, EstadoCivilAdm)
admin.site.register(models.GrauInstrucao, GrauInstrucaoAdm)
admin.site.register(models.Deficiencia, DeficienciaAdm)
admin.site.register(models.Nacionalidade, NacionalidadeAdm)
admin.site.register(models.UF, UFAdm)
admin.site.register(models.Cidade, CidadeAdm)
admin.site.register(models.Funcionario, FuncionarioAdm)
