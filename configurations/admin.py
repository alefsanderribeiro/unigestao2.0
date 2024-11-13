from django.contrib import admin
from .models import *

@admin.register(AdmissionType)
class AdmissionTypeAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    list_filter = ('description',)
    ordering = ('description',)

@admin.register(HarmfulExposure)
class HarmfulExposureAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    list_filter = ('description',)
    ordering = ('description',)

@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    list_filter = ('description',)
    ordering = ('description',)

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    list_filter = ('description',)
    ordering = ('description',)

@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    list_filter = ('description',)
    ordering = ('description',)

@admin.register(PixType)
class PixTypeAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    list_filter = ('description',)
    ordering = ('description',)


@admin.register(Gender)
class SexoAdm(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    ordering = ('description',)


@admin.register(Race)
class RacaAdm(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    ordering = ('description',)


@admin.register(MaritalStatus)
class EstadoCivilAdm(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    ordering = ('description',)


@admin.register(DegreeInstruction)
class GrauInstrucaoAdm(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    ordering = ('description',)


@admin.register(Deficiency)
class DeficienciaAdm(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    ordering = ('description',)


@admin.register(Nationality)
class NacionalidadeAdm(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    ordering = ('description',)
