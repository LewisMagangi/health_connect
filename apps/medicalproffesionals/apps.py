from django.apps import AppConfig

class MedicalProfessionalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.medicalproffesionals'
    verbose_name = 'Medical Professionals'

    def ready(self):
        # Remove signals import since we're not using it yet
        pass
