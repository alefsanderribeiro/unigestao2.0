# from django.contrib import admin
# from .models import CBO, Occupation, Synonym

# class SynonymInline(admin.TabularInline):
#     model = Synonym
#     extra = 1

# class OccupationInline(admin.TabularInline):
#     model = Occupation
#     extra = 1
#     inlines = [SynonymInline]

# @admin.register(CBO)
# class CBOAdmin(admin.ModelAdmin):
#     list_display = ('code', 'occupation')
#     search_fields = ('code', 'occupation')
#     inlines = [OccupationInline]


from django.contrib import admin
from .models import CBO, Occupation, Synonym

class SynonymInline(admin.TabularInline):
    model = Synonym
    extra = 1  # Número de linhas extras para adicionar novos sinônimos

class OccupationInline(admin.TabularInline):
    model = Occupation
    extra = 1  # Número de linhas extras para adicionar novas ocupações

@admin.register(CBO)
class CBOAdmin(admin.ModelAdmin):
    list_display = ('code', 'occupation')
    search_fields = ('code', 'occupation')
    
    fieldsets = [
        ('General', {'fields': ['code', 'occupation']}),
    ]
    
    inlines = [OccupationInline]
    ordering = ('occupation',)

@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = ('name', 'cbo')
    search_fields = ('name', 'cbo__code')
    
    inlines = [SynonymInline]
