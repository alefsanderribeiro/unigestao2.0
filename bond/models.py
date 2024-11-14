from django.db import models
from employees.models import Employee
from cbos.models import CBO
from configurations.models import (AdmissionType, HarmfulExposure,
                                   PaymentType, Bank, AccountType,
                                   PixType)


class AdmissionInfo(models.Model):
    employee = models.ForeignKey(Employee, related_name='admission_info', on_delete=models.CASCADE, verbose_name='Funcionário')
    cbo = models.ForeignKey(CBO, related_name='admission_info', on_delete=models.CASCADE, verbose_name='CBO')
    admission_type = models.ForeignKey(AdmissionType, on_delete=models.CASCADE, verbose_name='Tipo de Admissão')
    harmful_exposure = models.ForeignKey(HarmfulExposure, on_delete=models.CASCADE, verbose_name='Exposição a Agentes Nocivos')
    admission_date = models.DateField(verbose_name="Data de Admissão")
    experience_contract_days = models.IntegerField(blank=True, null=True, verbose_name="Nº de Dias em Contrato de Experiência")
    experience_extension_days = models.IntegerField(blank=True, null=True, verbose_name="Nº de Dias de Prorrogação em Contrato de Experiência")

    # Cargos
    position_01 = models.CharField(blank=True, null=True, max_length=100, verbose_name="Cargo 01")
    position_02 = models.CharField(blank=True, null=True, max_length=100, verbose_name="Cargo 02")
    change_date = models.DateField(blank=True, null=True, verbose_name="Data da Alteração")

    # Salários
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, verbose_name="Tipo de Pagamento")
    salary_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor do Salário")
    monthly_hours = models.IntegerField(verbose_name="Nº de Horas Mensais")
    inclusion_date = models.DateField(verbose_name="Data de Inclusão do Salário")

    # Informações Bancárias
    bank = models.ForeignKey(Bank, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Banco")
    agency = models.CharField(blank=True, null=True, max_length=10, verbose_name="Agência")
    account_type = models.ForeignKey(AccountType, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Tipo de Conta")
    account_number = models.CharField(blank=True, null=True, max_length=20, verbose_name="Nº Conta")
    check_digit = models.CharField(blank=True, null=True, max_length=5, verbose_name="Dígito Verificador")
    operation = models.CharField(max_length=10, null=True, blank=True, verbose_name="Operação")
    pix = models.CharField(max_length=50, null=True, blank=True, verbose_name="PIX")
    pix_type = models.ForeignKey(PixType, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Tipo de PIX")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    def __str__(self):
        return f"{self.employee} - Admissão em {self.admission_date}"

    class Meta:
        verbose_name = 'Informação de Admissão'
        verbose_name_plural = 'Informações de Admissão'
