from django.db import models
from django.conf import settings

class MedicalProfessional(models.Model):  # Renamed from MedicalProfessionalsMedicalprofessional
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50, unique=True)
    specialization = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'medical_professionals'  # Simplified table name
        verbose_name = 'Medical Professional'
        verbose_name_plural = 'Medical Professionals'
        ordering = ['user__last_name', 'user__first_name']

    def __str__(self):
        return f"Dr. {self.user.get_full_name()} - {self.specialization}"
