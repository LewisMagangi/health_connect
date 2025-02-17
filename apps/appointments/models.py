from django.db import models
from django.conf import settings
from apps.medicalproffesionals.models import MedicalProfessional

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('SCHEDULED', 'Scheduled'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )
    
    TYPE_CHOICES = (
        ('IN_PERSON', 'In Person'),
        ('VIRTUAL', 'Virtual'),
    )

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='appointments_as_patient'
    )
    provider = models.ForeignKey(
        MedicalProfessional,
        on_delete=models.CASCADE,
        related_name='appointments_as_provider'
    )
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SCHEDULED')
    appointment_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'appointments'
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
        ordering = ['-date_time']
        indexes = [
            models.Index(fields=['date_time', 'provider']),
            models.Index(fields=['patient', 'status']),
        ]

    def __str__(self):
        return f"{self.patient.get_full_name()} - {self.date_time}"
