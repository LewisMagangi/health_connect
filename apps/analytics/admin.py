from django.contrib import admin
from .models import UserActivity, HealthMetric  # Updated import

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'timestamp')
    list_filter = ('activity_type', 'timestamp')
    search_fields = ('user__username', 'activity_type')

@admin.register(HealthMetric)  # Updated registration
class HealthMetricAdmin(admin.ModelAdmin):
    list_display = ('patient', 'metric_type', 'value', 'recorded_at')
    list_filter = ('metric_type', 'recorded_at')
    search_fields = ('patient__username', 'metric_type')
