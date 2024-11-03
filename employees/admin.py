from django.contrib import admin
from . import models

@admin.register(models.Sexo)
class SexoAdm(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


@admin.register(models.Raca)
class RacaAdm(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


@admin.register(models.EstadoCivil)
class EstadoCivilAdm(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


@admin.register(models.GrauInstrucao)
class GrauInstrucaoAdm(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


@admin.register(models.Deficiencia)
class DeficienciaAdm(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


@admin.register(models.Nacionalidade)
class NacionalidadeAdm(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


@admin.register(models.UF)
class UFAdm(admin.ModelAdmin):
    list_display = ('sigla','nome',)
    search_fields = ('sigla',)


@admin.register(models.Cidade)
class CidadeAdm(admin.ModelAdmin):
    list_display = ('nome','uf',)
    search_fields = ('nome',)


@admin.register(models.Funcionario)
class FuncionarioAdm(admin.ModelAdmin):
    list_display = ('nome_completo','cpf','telefone', 'is_active',)
    search_fields = ('nome_completo',)
    list_filter = ('is_active',)
