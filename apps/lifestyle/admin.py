from django.contrib import admin
from .models import WellnessPlan, HealthMetric

@admin.register(WellnessPlan)
class WellnessPlanAdmin(admin.ModelAdmin):
    list_display = ('patient', 'title', 'status', 'start_date', 'end_date')
    list_filter = ('status', 'start_date')
    search_fields = ('patient__username', 'title')

@admin.register(HealthMetric)
class HealthMetricAdmin(admin.ModelAdmin):
    list_display = ('patient', 'metric_type', 'recorded_at')
    list_filter = ('metric_type', 'recorded_at')
    search_fields = ('patient__username',)
