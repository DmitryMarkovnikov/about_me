from django.db import models

# Create your models here.

class Job(models.Model):

    def __str__(self):
        if self.name:
            return 'Job: ' + self.name

    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
