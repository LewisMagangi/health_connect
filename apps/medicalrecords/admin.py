from django.contrib import admin
from .models import MedicalRecord, Consultation

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'blood_type', 'get_created_at', 'get_updated_at')
    list_filter = ('blood_type', 'created_at', 'updated_at')
    search_fields = ('patient__username', 'patient__email', 'medical_conditions', 'allergies')
    readonly_fields = ('get_created_at', 'get_updated_at')
    fieldsets = (
        ('Patient Information', {
            'fields': ('patient', 'blood_type')
        }),
        ('Medical Details', {
            'fields': ('allergies', 'medical_conditions', 'medications', 'immunizations')
        }),
        ('Additional Information', {
            'fields': ('notes', 'get_created_at', 'get_updated_at')
        }),
    )

    def get_created_at(self, obj):
        return obj.created_at
    get_created_at.short_description = 'Created At'

    def get_updated_at(self, obj):
        return obj.updated_at
    get_updated_at.short_description = 'Updated At'

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'provider', 'date', 'diagnosis')
    list_filter = ('date', 'provider')
    search_fields = ('patient__username', 'provider__user__username', 'diagnosis', 'symptoms')
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at')
