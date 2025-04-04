from django.db import models

class Feature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='features/')

    def __str__(self):
        return self.title
