from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=20)

class Message(models.Model):
    value = models.CharField(max_length=5000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    froms = models.ForeignKey(User,on_delete=models.CASCADE,related_name='SENDER')
    # room = models.CharField(max_length=100)
    to=models.ForeignKey(User,on_delete=models.CASCADE,related_name='RECEVER')