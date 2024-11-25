# Generated by Django 5.1.2 on 2024-11-24 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0008_payment_created_at_payment_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Desconto'),
        ),
        migrations.AddField(
            model_name='payment',
            name='discount_observation',
            field=models.TextField(blank=True, null=True, verbose_name='Observação do desconto'),
        ),
    ]
