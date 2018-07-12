from django.db import models

# Create your models here.


class Job(models.Model):

    def __str__(self):
        return self.position_name

    position_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    details = models.TextField()
    dates_of_work = models.CharField(max_length=200)
