from django.db import models

# Create your models here.
class trafficData(models.Model):
    location = models.CharField(max_length = 255)
    timestamp = models.DateTimeField()
    vehicle_count = models.IntegerField()
    average_speed = models.FloatField()
    
    def __str__(self):
        return f'traffic at {self.location} at {self.timestamp}'