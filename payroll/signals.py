from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Payment
from django.utils.timezone import now
from datetime import date


@receiver(pre_save, sender=Payment)
def pre_save_payment_handler(sender, instance, **kwargs):
    # Obtém o vínculo e calcula os ajustes
    if instance.bond:
        salary_value = instance.bond.salary_value  # Obtém o salário do vínculo
        adjusted_amount = salary_value - (instance.advance or 0) - (instance.discount or 0)

        # Define pagamentos parciais com base no tipo de pagamento
        payment_type = str(instance.bond.payment_type).lower() if instance.bond.payment_type else 'mensal'
        if payment_type == 'semanal':
            # Divide o valor em 4 partes
            partial_payment = adjusted_amount / 4
            instance.first_payment_amount = partial_payment
            instance.second_payment_amount = partial_payment
            instance.third_payment_amount = partial_payment
            instance.fourth_payment_amount = partial_payment
        elif payment_type == 'quinzenal':
            # Divide o valor em 2 partes
            partial_payment = adjusted_amount / 2
            instance.first_payment_amount = partial_payment
            instance.second_payment_amount = partial_payment

        # Adicionando o dia de vencimento do salário igual ao dia de inclusão
        if not instance.due_date:
            today = date.today()
            day = instance.bond.inclusion_date.day  # Recuperando o dia da inclusão do salário
            due_date = today.replace(day=day)
            instance.due_date = due_date

    # Atualiza o status do pagamento
    if not instance.payment_date and instance.due_date < now().date() and not any([
        instance.first_payment_date,
        instance.second_payment_date,
        instance.third_payment_date,
        instance.fourth_payment_date
    ]):
        # Se não há nenhuma data de pagamento (nem data de pagamento nem parciais)
        instance.status = 'overdue'
    elif instance.payment_date:
        # Se já existe data de pagamento, status é 'completed'
        instance.status = 'completed'
    else:
        # Verifica se alguma das datas de pagamento parciais está preenchida
        if any([
            instance.first_payment_date,
            instance.second_payment_date,
            instance.third_payment_date,
            instance.fourth_payment_date
        ]):
            # Se qualquer pagamento parcial tiver data, considera como em progresso
            instance.status = 'in_progress'
        else:
            # Se não tiver data de pagamento nem data parcial, é pendente
            instance.status = 'pending'

    # Calcula a soma dos pagamentos parciais, considerando apenas os valores preenchidos
    total_partial_amount = sum(filter(None, [
        instance.first_payment_amount,
        instance.second_payment_amount,
        instance.third_payment_amount,
        instance.fourth_payment_amount,
    ]))

    # Calcula o saldo devedor, ajustando pelo adiantamento e descontos
    salary_value = instance.bond.salary_value
    adjusted_advance = (instance.advance or 0) - (instance.discount or 0)
    remaining_salary = salary_value - total_partial_amount  # Saldo devedor

    # Valida se o adiantamento solicitado não ultrapassa o saldo devedor
    if adjusted_advance > remaining_salary:
        raise ValidationError(
            f'O adiantamento solicitado (R${adjusted_advance}) não pode ultrapassar o saldo devedor (R${remaining_salary}).'
        )

    # Verifica se o total dos pagamentos parciais e adiantamento não excede o salário
    if total_partial_amount + adjusted_advance > salary_value:
        raise ValidationError(
            f'O total dos pagamentos parciais e adiantamento não pode exceder o valor total do salário (R${salary_value}).'
        )
