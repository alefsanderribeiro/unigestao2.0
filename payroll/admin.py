from django.contrib import admin
from django.utils import timezone
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Pagamento', {
            'fields': ('bond', 'payment_date', 'due_date',
                       'advance', 'notes')
        }),

        ('Pagamentos Parciais', {
            'fields': ('first_payment_date', 'first_payment_amount',
                       'second_payment_date', 'second_payment_amount',
                       'third_payment_date', 'third_payment_amount',
                       'fourth_payment_date', 'fourth_payment_amount')
        }),

        ('Descontos', {
            'fields': ('discount', 'discount_observation')
        })
    )
    list_display = ('bond', 'due_date', 'payment_date',
                    'advance', 'discount', 'adjusted_amount', 'notes',
                    'status',)
    list_filter = ('status', 'due_date', 'payment_date')
    search_fields = ('bond__employee__full_name',)
    date_hierarchy = 'due_date'

    # Adiciona o método get_adjusted_amount como uma coluna no admin
    def adjusted_amount(self, obj):
        return obj.get_adjusted_amount()

    # Adiciona títulos personalizados para os métodos
    adjusted_amount.short_description = 'Valor Ajustado'

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed', payment_date=timezone.now().date())
    mark_as_completed.short_description = 'Marcar como concluído'

    actions = [mark_as_completed]
