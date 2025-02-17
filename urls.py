from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('', views.home, name='home'),  # Add home page URL
    path('accounts/login/', views.login_view, name='login'),  # Changed back to 'accounts/login/'
]