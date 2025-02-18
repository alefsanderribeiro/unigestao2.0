# Generated by Django 5.1.2 on 2025-02-16 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Conta',
                'verbose_name_plural': 'Tipos de Conta',
            },
        ),
        migrations.CreateModel(
            name='AdmissionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Admissão',
                'verbose_name_plural': 'Tipos de Admissão',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Banco',
                'verbose_name_plural': 'Bancos',
            },
        ),
        migrations.CreateModel(
            name='Deficiency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Deficiência',
                'verbose_name_plural': 'Deficiência',
            },
        ),
        migrations.CreateModel(
            name='DegreeInstruction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Grau de Instrução',
                'verbose_name_plural': 'Grau de Instrução',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
            },
        ),
        migrations.CreateModel(
            name='HarmfulExposure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Exposição a Agentes Nocivos',
                'verbose_name_plural': 'Exposições a Agentes Nocivos',
            },
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Estado Civil',
                'verbose_name_plural': 'Estado Civil',
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Nacionalidade',
                'verbose_name_plural': 'Nacionalidade',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Pagamento',
                'verbose_name_plural': 'Tipos de Pagamento',
            },
        ),
        migrations.CreateModel(
            name='PixType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Tipo de Pix',
                'verbose_name_plural': 'Tipos de Pix',
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Raça',
                'verbose_name_plural': 'Raça',
            },
        ),
    ]
