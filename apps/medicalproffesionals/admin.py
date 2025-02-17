from django.contrib import admin
from .models import MedicalProfessional

@admin.register(MedicalProfessional)
class MedicalProfessionalAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_number', 'specialization', 'years_of_experience', 'is_active')
    list_filter = ('is_active', 'specialization')
    search_fields = ('user__username', 'user__email', 'license_number')
    ordering = ('user__last_name', 'user__first_name')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
