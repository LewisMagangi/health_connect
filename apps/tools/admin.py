from django.contrib import admin
from .models import HealthCalculator, CalculationHistory

@admin.register(HealthCalculator)
class HealthCalculatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'calculator_type', 'is_active')
    list_filter = ('calculator_type', 'is_active')
    search_fields = ('name', 'description')

@admin.register(CalculationHistory)
class CalculationHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'calculator', 'calculated_at')
    list_filter = ('calculator', 'calculated_at')
    search_fields = ('user__username',)
    date_hierarchy = 'calculated_at'
