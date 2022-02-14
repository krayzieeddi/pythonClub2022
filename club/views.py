from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event
from django.shortcuts import  get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def getResources(request):
    resource_list = Resource.objects.all()
    return render(request, 'club/resources.html' ,{'resource_list' : resource_list})

def getMeetings(request):
    meetings_list = Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meetings_list': meetings_list})

def getMeetingDetails(request, id):
    meet = get_object_or_404(Meeting, pk=id)
    meetDetails = meet.meetingdescription
    context = {
        'meet' : meet,
        'meetDetails' : meetDetails,
    }
    return render(request, 'club/meetingDetails.html', context=context)