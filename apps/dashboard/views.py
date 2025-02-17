from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from apps.appointments.models import Appointment
from datetime import date, timedelta
from django.utils import timezone

User = get_user_model()

def is_admin(user):
    return user.is_staff

def is_doctor(user):
    return user.user_type == 'PROVIDER'

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    today = timezone.now().date()
    context = {
        'total_users': User.objects.count(),
        'active_doctors': User.objects.filter(
            user_type='PROVIDER',
            is_active=True
        ).count(),
        'appointments_today': Appointment.objects.filter(
            date_time__date=today
        ).count(),
        'recent_activities': []
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

@login_required
@user_passes_test(is_doctor)
def doctor_dashboard(request):
    today = timezone.now().date()
    context = {
        'today_appointments': Appointment.objects.filter(
            provider=request.user,
            date_time__date=today
        ).order_by('date_time'),
        'total_patients': Appointment.objects.filter(provider=request.user).values('patient').distinct().count(),
        'appointments_week': Appointment.objects.filter(
            provider=request.user,
            date_time__date__range=[today, today + timedelta(days=7)]
        ).count(),
        'pending_reports': 0  # Implement this based on your medical records system
    }
    return render(request, 'dashboard/doctor_dashboard.html', context)

@login_required
def patient_dashboard(request):
    if request.user.is_staff:
        return redirect('dashboard:admin_dashboard')
    elif request.user.user_type == 'PROVIDER':
        return redirect('dashboard:doctor_dashboard')
    
    now = timezone.now()
    context = {
        'upcoming_appointments': Appointment.objects.filter(
            patient=request.user,
            date_time__gt=now
        ).order_by('date_time')[:5],
        'last_checkup': Appointment.objects.filter(
            patient=request.user,
            date_time__lt=now
        ).order_by('-date_time').first(),
        'next_appointment': Appointment.objects.filter(
            patient=request.user,
            date_time__gt=now
        ).order_by('date_time').first(),
        'pending_tests': 0  # Implement this based on your medical records system
    }
    return render(request, 'dashboard/patient_dashboard.html', context)
