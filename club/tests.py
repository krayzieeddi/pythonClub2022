from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm

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