from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type = Meeting(meetingName = 'meeting1')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'meeting1')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting') # this tests the real name of table within current db

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.type = Meeting(meetingName = 'meeting1')
        self.meetingMinutes = MeetingMinutes(meetingId = self.type, minutesText = '5 minutes')
        
    def test_text(self):
        self.assertEqual(str(self.meetingMinutes.minutesText), '5 minutes')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingMinutes')

class ResourceTest(TestCase):
    def setUp(self):
        self.type = Resource(resourceName = 'resource1')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'resource1')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource') 

class EventTest(TestCase):
    def setUp(self):
        self.type = Event(eventTitle = 'event1')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'event1')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event') 

class NewMeetingForm(TestCase):
    #valid form data
    def test_meetingForm(self):
        form = MeetingForm (data={'meetingName' : 'da name', 'meetingDesciption' : 'its a meeting'})
        self.assertTrue(form.is_valid())

class New_Meeting_authentication_Test(TestCase):
    def setup(self):
        self.test_user=User.objects.create_user(username='testuser1', password='password')
        self.type=Meeting.objects.create(meetingName='the meeting')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newMeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newMeeting/')