from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.getResources, name='resources'),
    path('meetings/', views.getMeetings, name='meetings'),
    path('meetingDetails/<int:id>', views.getMeetingDetails, name='meetingDetails'),
    path('newMeeting/' , views.newMeeting, name = 'newMeeting'),
]