from django.db import models

class Post(models.Model):

    def __str__(self):
        if self.name:
            return 'Post: ' + self.name
                        
    name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    pub_data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
