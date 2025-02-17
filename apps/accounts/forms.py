from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ProfileStepTwoForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    user_type = forms.ChoiceField(
        choices=[
            ('PATIENT', 'Patient'),
            ('PROVIDER', 'Healthcare Provider')
        ],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'user_type')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('date_of_birth', 'phone_number', 'address', 
                 'emergency_contact_name', 'emergency_contact_phone',
                 'medical_conditions')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'medical_conditions': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }
