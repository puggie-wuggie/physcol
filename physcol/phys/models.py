from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    speaker = models.ForeignKey('Speaker')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    local_contact0 = models.ForeignKey(User, related_name='+')
    local_contact1 = models.ForeignKey(User,related_name='+')
    audience = models.CharField(max_length=100)
    details = models.CharField(max_length=2048)

class Speaker(models.Model):
#to be filled
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    affiliation = models.CharField(max_length=1028)
    details = models.CharField(max_length=2048)

class Submission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=524)
    affiliation = models.CharField(max_length=2048)
    research = models.CharField(max_length=2048)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    vote_count = models.IntegerField()

class Itinerary(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey('Event')
    speaker_id = models.ForeignKey('Speaker')
    createdby_id = models.ForeignKey(User)
    notes = models.CharField(max_length=2048)
