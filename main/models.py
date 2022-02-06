from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone 
import uuid


# Users
class User(AbstractUser):
    pass

class Person(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)    
    eeid = models.IntegerField()
    msid = models.CharField(max_length=20)
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return f'{self.eeid}, {self.msid}'

class Activities(models.Model):
    act = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.act}'

class Sch_Time(models.Model):
    sch_from = models.TimeField()
    sch_to = models.TimeField()
    sch_activity = models.ForeignKey(Activities, related_name='sch_activity', null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.sch_from}, to  {self.sch_to}, {self.sch_activity}'

    

class Shift(models.Model):
    shift_id = models.CharField(default=uuid.uuid4, max_length=100)
    date = models.DateField()   
    shift_person = models.ForeignKey(Person, related_name='shift_person', null=True, on_delete=models.CASCADE) 
    time_len = models.IntegerField(default=0) # Shift durations in minutes    
    sch_time_range = models.ManyToManyField(Sch_Time)    
   
    def __str__(self):
        return f'{self.shift_person.name}, {self.date} '
    