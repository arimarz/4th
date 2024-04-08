from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Participant(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.EmailField(unique=True)
    registered_events = models.ManyToManyField(Event)

class EventFeedback(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, unique=True)
    feedback_text = models.TextField()
    rating = models.IntegerField()
