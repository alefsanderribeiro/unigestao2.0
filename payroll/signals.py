from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Payment
from django.utils.timezone import now


@receiver(pre_save, sender=Payment)
def pre_save_payment_handler(sender, instance, **kwargs):
    # Obtém o vínculo e calcula os ajustes
    if instance.bond:
        salary_value = instance.bond.salary_value  # Obtém o salário do vínculo
        adjusted_amount = salary_value - (instance.advance or 0)

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
