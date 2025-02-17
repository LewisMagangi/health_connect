from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MedicalRecord

@login_required
def records_home(request):
    """Home view for medical records"""
    if request.user.is_staff:
        records = MedicalRecord.objects.all()
    else:
        records = MedicalRecord.objects.filter(patient=request.user)

    context = {
        'records': records,
        'health_summary': {
            'height': '175 cm',  # Replace with actual data
            'weight': '70 kg',
            'blood_type': 'A+',
            'allergies': []
        }
    }
    return render(request, 'medicalrecords/list.html', context)

@login_required
def record_detail(request, pk):
    """View for individual medical record"""
    record = get_object_or_404(MedicalRecord, pk=pk)
    if not request.user.is_staff and record.patient != request.user:
        messages.error(request, "You don't have permission to view this record.")
        return redirect('medicalrecords:list')
    return render(request, 'medicalrecords/detail.html', {'record': record})

@login_required
def download_records(request):
    """View for downloading medical records"""
    messages.info(request, "Download feature coming soon!")
    return redirect('medicalrecords:list')

@login_required
def share_records(request):
    """View for sharing medical records"""
    messages.info(request, "Sharing feature coming soon!")
    return redirect('medicalrecords:list')

@login_required
def create_medical_record(request):
    # Add create view logic here
    pass

@login_required
def edit_medical_record(request, record_id):
    # Add edit view logic here
    pass
