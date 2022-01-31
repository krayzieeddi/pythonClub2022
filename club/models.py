from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meetingName = models.CharField(max_length = 255)
    meetingdescription = models.TextField(max_length = 255, null = True, blank = True)

    def __str__(self):
        return self.meetingName

    class Meta:
        db_table = 'meeting'
        verbose_name_plural='meetings'

class MeetingMinutes(models.Model):
    meetingId = models.ForeignKey(Meeting, on_delete = models.DO_NOTHING)
    attendence = models.ManyToManyField(User)
    minutesText = models.TextField(max_length = 255, null = True, blank = True)

    def __str__(self):
        return self.meetingId

    class Meta:
        db_table = 'meetingMinutes'

class Resource(models.Model):
    resourceName = models.CharField(max_length = 255)
    resourceType = models.CharField(max_length = 255)
    resourceUrl = models.URLField(null=True, blank=True)
    dateEntered = models.DateField()
    userId = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    resourceDescription = models.TextField(max_length = 255, null = True, blank = True)

    def __str__(self):
        return self.resourceName

    class Meta:
        db_table = 'resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventTitle = models.CharField(max_length = 255)
    eventLocation = models.CharField(max_length = 255)
    eventDate = models.DateField()
    eventTime = models.CharField(max_length = 255)
    eventDescription = models.TextField()
    userId = models.CharField(max_length = 255)

    def __str__(self):
        return self.eventTitle

    class Meta:
        db_table = 'event'
        verbose_name_plural='events'