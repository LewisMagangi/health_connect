from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:  # Redirects to login if not authenticated
            return redirect('dashboard:admin_dashboard')
        elif request.user.user_type == 'PROVIDER':
            return redirect('dashboard:doctor_dashboard')
        else:
            return redirect('dashboard:patient_dashboard')
    
    return render(request, 'home.html')  # Show landing page for non-authenticated users
