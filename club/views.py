from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event
from django.shortcuts import  get_object_or_404
from .forms import MeetingForm
from django.contrib.auth.decorators import login_required

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

@login_required
def newMeeting(request):
    form = MeetingForm

    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'club/newMeeting.html', {'form': form})

def loginMessage(request):
    return render(request, 'club/loginMessage.html')

def logOutMessage(request):
    return render(request, 'club/logOutMessage.html')