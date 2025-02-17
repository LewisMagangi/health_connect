from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('', views.analytics_dashboard, name='analytics_dashboard'),
    path('patients/', views.patient_analytics, name='patient_analytics'),
    path('appointments/', views.appointment_analytics, name='appointment_analytics'),
    path('revenue/', views.revenue_analytics, name='revenue_analytics'),
]
