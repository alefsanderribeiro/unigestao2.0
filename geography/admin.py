from django.contrib import admin
from .models import Country, State, Capital, City, Region

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'code', 'country')
    search_fields = ('name',)

@admin.register(Capital)
class CapitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'country')
    search_fields = ('name',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state')
    search_fields = ('name',)

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)
