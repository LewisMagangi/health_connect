from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import get_user_model
from .forms import (
    UserRegistrationForm,
    LoginForm,
    ProfileStepTwoForm,
    UserProfileForm
)
from apps.users.models import UserProfile  # Updated from Profile to UserProfile

User = get_user_model()

def register_step_one(request):
    if request.method == 'POST':
        form = RegistrationStepOneForm(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                request.session['registration_user_id'] = user.id
                return redirect('accounts:register_step_two')
            except Exception as e:
                messages.error(request, 'An error occurred during registration.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = RegistrationStepOneForm()

    return render(request, 'accounts/register_step_one.html', {'form': form})

@login_required
def register_step_two(request):
    if request.method == 'POST':
        form = ProfileStepTwoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile information updated!')
            return redirect('accounts:complete_profile')
    else:
        form = ProfileStepTwoForm(instance=request.user)
    return render(request, 'accounts/register_step_two.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'accounts/login.html', {
        'form': LoginForm()
    })

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('accounts:register_step_two')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def logout_view(request):
    username = request.user.username  # Get username before logout
    logout(request)
    messages.success(request, f'Goodbye {username}! You have been successfully logged out.')
    return redirect('accounts:login')

@login_required
def complete_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile completed successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=request.user.profile)
    
    return render(request, 'accounts/complete_profile.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=request.user.profile)
    
    return render(request, 'accounts/profile.html', {'form': form})
