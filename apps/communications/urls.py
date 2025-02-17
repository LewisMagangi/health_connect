from django.urls import path
from . import views

app_name = 'messages'

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('compose/', views.compose, name='compose'),
    path('message/<int:pk>/', views.message_detail, name='detail'),
]
