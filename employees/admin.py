import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class FuncionarioAdm(admin.ModelAdmin):
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('full_name', 'gender', 'race', 'marital_status',
                       'birth_date', 'degree_instruction', 'deficiency',
                       'nationality', 'mother_name', 'father_name', 'is_active',)
        }),

        ('Naturalidade', {
            'fields': ('naturalness_uf', 'natural_city')
        }),

        ('Documentos', {
            'fields': ('cpf', 'pis_nis', 'military_certificate', 'identity_number',
                       'date_emission_identity', 'organ_consignor_identity',
                       'uf_identity')
        }),

        ('Carteira de trabalho', {
            'fields': ('number_ctps', 'series_ctps', 'date_emission_ctps', 'uf_ctps',)
        }),

        ('Dados complementares', {
            'fields': ('cep', 'address_uf', 'city_address', 'neighborhood',
                       'number', 'complement')
        }),

        ('Contato', {
            'fields': ('contact', 'telephone', 'email')
        })
    )

    list_display = ('full_name', 'gender', 'birth_date', 'cpf', 'telephone', 'is_active',)
    search_fields = ('full_name',)
    list_filter = ('is_active',)
    ordering = ('full_name',)

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employees.csv"'
        writer = csv.writer(response)
        writer.writerow(['nome_completo', 'cpf', 'telefone', 'ativo',])

        for funcionario in queryset:
            writer.writerow([funcionario.full_name, funcionario.cpf, funcionario.telephone, funcionario.is_active])

        self.message_user(request, f'{queryset.count()} funcionários exportados com sucesso.')
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]
