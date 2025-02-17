from django.db import models
from django.conf import settings

class MedicalRecord(models.Model):
    # ...existing code...

    class Meta:
        verbose_name = 'Medical Record'
        verbose_name_plural = 'Medical Records'
        db_table = 'medical_records_medicalrecord'  # Updated table name

class Consultation(models.Model):
    # ...existing code...

    class Meta:
        verbose_name = 'Consultation'
        verbose_name_plural = 'Consultations'
        db_table = 'medical_records_consultation'  # Updated table name
