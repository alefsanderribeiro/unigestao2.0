from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from bond.models import AdmissionInfo


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('completed', 'Concluído'),
        ('overdue', 'Atrasado'),
        ('in_progress', 'Em Andamento'),
    ]

    bond = models.ForeignKey(AdmissionInfo, on_delete=models.CASCADE, related_name='payments', verbose_name='Vínculo')
    payment_date = models.DateField(blank=True, null=True, verbose_name='Data de Pagamento')
    due_date = models.DateField(null=True, blank=True, verbose_name='Data de Vencimento')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Status')
    notes = models.TextField(blank=True, null=True, verbose_name='Observações')
    advance = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, default=0, verbose_name='Adiantamento')

    # Campo para inserir descontos
    discount = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, default=0, verbose_name='Desconto')
    discount_observation = models.TextField(blank=True, null=True, verbose_name='Observação do desconto')

    # Campos para registrar pagamentos parciais
    first_payment_date = models.DateField(blank=True, null=True, verbose_name='Data do Primeiro Pagamento Parcial')
    first_payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Valor do Primeiro Pagamento Parcial')

    second_payment_date = models.DateField(blank=True, null=True, verbose_name='Data do Segundo Pagamento Parcial')
    second_payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Valor do Segundo Pagamento Parcial')

    third_payment_date = models.DateField(blank=True, null=True, verbose_name='Data do Terceiro Pagamento Parcial')
    third_payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Valor do Terceiro Pagamento Parcial')

    fourth_payment_date = models.DateField(blank=True, null=True, verbose_name='Data do Quarto Pagamento Parcial')
    fourth_payment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Valor do Quarto Pagamento Parcial')

    # Campos de Auditoria
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        self.employee_active_clean()
        self.date_validation_clean()
        self.partial_payment_clean()

    def employee_active_clean(self):
        # Verifica se o funcionário está ativo antes de permitir o pagamento
        if not self.bond.employee.is_active:
            raise ValidationError('O pagamento não pode ser feito para um funcionário inativo.')

    def date_validation_clean(self):
        # Verifica se a data do pagamento é válida
        if self.payment_date and self.payment_date > timezone.localtime(timezone.now()).date():
            raise ValidationError('A data de pagamento não pode ser maior que a data atual.')

        # Verifica se as datas dos pagamentos parciais são válidas
        partial_dates = {
            'Data do Primeiro Pagamento': self.first_payment_date,
            'Data do Segundo Pagamento': self.second_payment_date,
            'Data do Terceiro Pagamento': self.third_payment_date,
            'Data do Quarto Pagamento': self.fourth_payment_date,
        }

        for label, date in partial_dates.items():
            if date and date > timezone.localtime(timezone.now()).date():
                raise ValidationError(
                    f'{label} não pode ser maior que a data atual.'
                )

        # Validação para as datas de pagamento parciais
        partial_dates = [
            ('Data do Primeiro Pagamento', self.first_payment_date),
            ('Data do Segundo Pagamento', self.second_payment_date),
            ('Data do Terceiro Pagamento', self.third_payment_date),
            ('Data do Quarto Pagamento', self.fourth_payment_date),
        ]

        for i in range(1, len(partial_dates)):
            current_label, current_date = partial_dates[i]
            previous_label, previous_date = partial_dates[i - 1]

            if current_date and previous_date and current_date < previous_date:
                raise ValidationError(
                    f'{current_label} não pode ser menor que {previous_label}!'
                )

    def partial_payment_clean(self):
        # Valida que os pagamentos parciais não ultrapassam o valor ajustado
        salary_value = self.bond.salary_value - (self.advance or 0) - (self.discount or 0)  # Obtém o salário do vínculo com deduções caso tenha

        total_partial_amount = sum(
            filter(None, [
                self.first_payment_amount,
                self.second_payment_amount,
                self.third_payment_amount,
                self.fourth_payment_amount,
            ])
        )
        if total_partial_amount > salary_value:
            raise ValidationError(
                f'Os pagamentos parciais não podem exceder o valor total do salário (R${self.bond.salary_value}).'
            )

    def get_adjusted_amount(self):
        """
        Retorna o valor ajustado (valor total menos adiantamento e ou desconto).
        """
        return self.bond.salary_value - (self.advance or 0) - (self.discount or 0)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering = ['-due_date']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['due_date']),
        ]

    def __str__(self):
        return f'{self.bond} ({self.status})'
