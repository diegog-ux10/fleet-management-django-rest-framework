from django.db import models

class Taxi(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    plate = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['plate']
    
class Trayectory(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    taxi_id = models.ForeignKey(Taxi, on_delete=models.CASCADE)  
    latitude = models.FloatField()  
    longitude = models.FloatField()

    class Meta:
        ordering = ['date']