from django.db import models
from django.conf import settings

class WellnessPlan(models.Model):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('PAUSED', 'Paused'),
    )

    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    goals = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HealthMetric(models.Model):
    METRIC_TYPES = (
        ('WEIGHT', 'Weight'),
        ('BLOOD_PRESSURE', 'Blood Pressure'),
        ('HEART_RATE', 'Heart Rate'),
        ('SLEEP', 'Sleep'),
        ('EXERCISE', 'Exercise'),
    )

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lifestyle_health_metrics'  # Added related_name
    )
    metric_type = models.CharField(max_length=20, choices=METRIC_TYPES)
    value = models.JSONField()
    recorded_at = models.DateTimeField()
    notes = models.TextField(blank=True)
