from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def analytics_dashboard(request):
    context = {
        'title': 'Analytics Dashboard',
        # Add more context data as needed
    }
    return render(request, 'analytics/dashboard.html', context)

@login_required
@user_passes_test(is_staff)
def patient_analytics(request):
    return render(request, 'analytics/patients.html')

@login_required
@user_passes_test(is_staff)
def appointment_analytics(request):
    return render(request, 'analytics/appointments.html')

@login_required
@user_passes_test(is_staff)
def revenue_analytics(request):
    return render(request, 'analytics/revenue.html')
