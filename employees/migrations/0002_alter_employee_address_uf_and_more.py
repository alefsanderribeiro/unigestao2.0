# Generated by Django 5.1.2 on 2025-02-18 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address_uf',
            field=models.CharField(max_length=150, verbose_name='Estado (UF)'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='city_address',
            field=models.CharField(max_length=155, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='neighborhood',
            field=models.CharField(max_length=100, verbose_name='Bairro'),
        ),
    ]
