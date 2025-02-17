from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('register/step-two/', views.register_step_two, name='register_step_two'),
    path('profile/', views.profile, name='profile'),
    path('profile/complete/', views.complete_profile, name='complete_profile'),
]
