# Tools App Models

## HealthCalculator Model
Defines different health calculation tools.

```python
class HealthCalculator(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(choices=[
        ('BMI', 'Body Mass Index'),
        ('CALORIE', 'Calorie Counter'),
        ('HYDRATION', 'Hydration Calculator')
    ])
    formula = models.JSONField()
    description = models.TextField()
```

## AssessmentTool Model
Manages health assessment questionnaires.

```python
class AssessmentTool(models.Model):
    title = models.CharField(max_length=200)
    questions = models.JSONField()
    scoring_logic = models.JSONField()
    category = models.CharField(choices=[
        ('MENTAL_HEALTH', 'Mental Health'),
        ('PHYSICAL_FITNESS', 'Physical Fitness'),
        ('NUTRITION', 'Nutrition')
    ])
```
