from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_meeting, name='upload_meeting'),
    path('', views.meeting_list, name='meeting_list'),
]