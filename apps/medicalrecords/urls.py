from django.urls import path
from . import views

app_name = 'medicalrecords'

urlpatterns = [
    path('', views.records_home, name='list'),  # Changed to match the existing view
    path('<int:pk>/', views.record_detail, name='detail'),  # Updated to match view signature
    path('download/', views.download_records, name='download'),
    path('share/', views.share_records, name='share'),
]
