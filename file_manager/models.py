import os

from django.db import models
from employees.models import Employee


class NameFile(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nome do arquivo')

    class Meta:
        verbose_name = 'Nome do arquivo'
        verbose_name_plural = 'Nomes dos arquivos'

    def __str__(self):
        return self.name

def employee_directory_path(instance, filename):
    return f'file_manager/{instance.employee.id}/{filename}'


class File(models.Model):
    name_file = models.ForeignKey(NameFile, on_delete=models.CASCADE, related_name='files', verbose_name='Nome do arquivo')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='files', verbose_name='Funcionário')
    file = models.FileField(upload_to=employee_directory_path, verbose_name='Arquivo')
    upload_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado em')

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'

    def __str__(self):
        return f'{self.name_file} - {self.employee.full_name} - {self.file.name}'
