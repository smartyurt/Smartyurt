from django.db import models
from django.utils import timezone

class Feature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='features/')

    def __str__(self):
        return self.title


class SensorData(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    temperature = models.FloatField()
    humidity = models.FloatField()
    gas_concentration = models.FloatField()  # Убедитесь, что это поле есть
    sensor_id = models.CharField(max_length=100, blank=True, null=True)
    gas_type = models.CharField(max_length=100, choices=[('methane', 'Метан'), ('LPG', 'LPG'), ('CO', 'CO')],
                                default='methane')

    def __str__(self):
        return f"Данные сенсора на {self.timestamp} для сенсора ID {self.sensor_id}"
