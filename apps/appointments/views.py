from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment

@login_required
def appointment_list(request):
    """View for listing appointments"""
    appointments = Appointment.objects.filter(patient=request.user).order_by('date_time')
    return render(request, 'appointments/list.html', {
        'appointments': appointments
    })

@login_required
def schedule_appointment(request):
    """View for scheduling new appointments"""
    if request.method == 'POST':
        # Handle form submission
        # ...Add your form processing logic here...
        messages.success(request, 'Appointment scheduled successfully!')
        return redirect('appointments:list')
    
    return render(request, 'appointments/schedule.html', {
        'specialties': [] # Add your specialties query here
    })

@login_required
def appointment_detail(request, pk):
    """View for appointment details"""
    appointment = Appointment.objects.get(pk=pk, patient=request.user)
    return render(request, 'appointments/detail.html', {
        'appointment': appointment
    })

@login_required
def cancel_appointment(request, pk):
    """View for canceling appointments"""
    if request.method == 'POST':
        appointment = Appointment.objects.get(pk=pk, patient=request.user)
        appointment.status = 'CANCELLED'
        appointment.save()
        messages.success(request, 'Appointment cancelled successfully')
        return redirect('appointments:list')
    return redirect('appointments:detail', pk=pk)
