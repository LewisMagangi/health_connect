from django.db import models
from django.conf import settings

class HealthMetric(models.Model):  # Final name
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='analytics_health_metrics'  # Added related_name
    )
    metric_type = models.CharField(max_length=50)
    value = models.FloatField()
    recorded_at = models.DateTimeField()
    analysis_data = models.JSONField()

    class Meta:
        db_table = 'analytics_health_metrics'
        verbose_name = 'Health Metric'
        verbose_name_plural = 'Health Metrics'
        ordering = ['-recorded_at']

class UserActivity(models.Model):  # Renamed from AnalyticsUseractivity
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    activity_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    class Meta:
        verbose_name = 'User Activity'
        verbose_name_plural = 'User Activities'
        ordering = ['-timestamp']
        db_table = 'analytics_user_activity'  # Explicit table name
        indexes = [
            models.Index(fields=['user', 'activity_type']),
            models.Index(fields=['timestamp']),
        ]
