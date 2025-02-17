from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'provider', 'date_time', 'status', 'appointment_type')
    list_filter = ('status', 'appointment_type', 'date_time')
    search_fields = ('patient__username', 'provider__user__username', 'notes')
    date_hierarchy = 'date_time'

