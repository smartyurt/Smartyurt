from django.db import models

class Feature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='features/')

    def __str__(self):
        return self.title
class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
