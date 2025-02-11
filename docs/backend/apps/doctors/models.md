# Doctors App Models

## Specialization Model
Manages medical specialties and subspecialties.

```python
class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    parent_specialty = models.ForeignKey('self', null=True, blank=True)
```

## DoctorProfile Model
Extended doctor-specific information.

```python
class DoctorProfile(models.Model):
    user = models.OneToOneField('users.Provider')
    specializations = models.ManyToManyField(Specialization)
    education = models.TextField()
    certifications = models.TextField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
```
