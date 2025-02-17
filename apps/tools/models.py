from django.db import models
from django.conf import settings

class HealthCalculator(models.Model):
    name = models.CharField(max_length=100)
    calculator_type = models.CharField(max_length=50)
    description = models.TextField()
    formula = models.JSONField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'tools_health_calculator'
        verbose_name = 'Health Calculator'
        verbose_name_plural = 'Health Calculators'

class CalculationHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    calculator = models.ForeignKey(HealthCalculator, on_delete=models.CASCADE)
    input_data = models.JSONField()
    result = models.JSONField()
    calculated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tools_calculation_history'
        verbose_name = 'Calculation History'
        verbose_name_plural = 'Calculation Histories'
        ordering = ['-calculated_at']
