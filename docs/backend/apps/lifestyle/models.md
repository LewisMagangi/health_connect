# Lifestyle App Models

## WellnessPlan Model
Tracks patient wellness goals and progress.

```python
class WellnessPlan(models.Model):
    patient = models.ForeignKey('users.Patient')
    title = models.CharField(max_length=200)
    goals = models.JSONField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(choices=[
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('PAUSED', 'Paused')
    ])
```

## HealthMetrics Model
Records patient health measurements and activities.

```python
class HealthMetrics(models.Model):
    patient = models.ForeignKey('users.Patient')
    metric_type = models.CharField(choices=[
        ('WEIGHT', 'Weight'),
        ('BLOOD_PRESSURE', 'Blood Pressure'),
        ('ACTIVITY', 'Physical Activity'),
        ('SLEEP', 'Sleep Hours')
    ])
    value = models.JSONField()
    timestamp = models.DateTimeField()
```
