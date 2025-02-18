# Generated by Django 5.1.2 on 2025-02-17 00:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('file_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='file',
            name='name_file',
        ),
        migrations.CreateModel(
            name='FileEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Editado em')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='employees.employee', verbose_name='Funcionário')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='file_manager.file', verbose_name='Arquivo')),
                ('name_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='file_manager.namefile', verbose_name='Nome do arquivo')),
            ],
        ),
    ]
