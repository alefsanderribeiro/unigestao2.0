from django.contrib import admin
from .models import AdmissionInfo


@admin.register(AdmissionInfo)
class AdmissionInfoAdmin(admin.ModelAdmin):
    list_display = ('employee', 'admission_date', 'salary_value', 'bank', 'agency', 'account_number', 'pix')
    search_fields = ('employee__full_name', 'admission_date', 'salary_value')
    list_filter = ('admission_date', 'payment_type', 'bank', 'account_type')
    ordering = ('admission_date',)
