from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Pagamento', {
            'fields': ('employee', 'bond', 'payment_date', 'due_date',
                       'advance', 'notes')
        }),

        ('Pagamentos Parciais', {
            'fields': ('first_payment_date', 'first_payment_amount',
                       'second_payment_date', 'second_payment_amount',
                       'third_payment_date', 'third_payment_amount',
                       'fourth_payment_date', 'fourth_payment_amount')
        })
    )
    list_display = ('employee', 'bond', 'due_date', 'payment_date',
                    'advance', 'adjusted_amount', 'notes', 'status',)
    list_filter = ('status', 'due_date', 'payment_date')
    search_fields = ('employee__full_name',)
    date_hierarchy = 'due_date'

    # Adiciona o método get_adjusted_amount como uma coluna no admin
    def adjusted_amount(self, obj):
        return obj.get_adjusted_amount()

    # Adiciona títulos personalizados para os métodos
    adjusted_amount.short_description = 'Valor Ajustado'
