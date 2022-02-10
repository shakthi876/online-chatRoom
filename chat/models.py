from django.db import models
""" import datetime
from datetime import datetime,date

now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")




 
# Returns the current local date
today = date.today().strftime('%d/%m/%Y') """



# Create your models here.
class Room(models.Model):
    room = models.CharField(max_length=1000)

    def __str__(self):
        return self.room

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.CharField(max_length=15)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    time = models.CharField(max_length=15)
   

    def __str__(self):
        return self.user