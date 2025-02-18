from django.contrib import admin
from .models import NameFile, File


class FileInline(admin.TabularInline):
    model = File
    extra = 1


@admin.register(NameFile)
class NameFileAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    # inlines = [FileInline]


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name_file', 'employee', 'file', 'upload_date', 'updated_at')
    search_fields = ('name_file' ,'employee', 'file', 'upload_date')
    ordering = ('name_file', 'employee', 'upload_date', 'updated_at')
