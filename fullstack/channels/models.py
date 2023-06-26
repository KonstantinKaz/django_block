from django.db import models
from django.contrib.auth.models import User

class Channel(models.Model):
    image = models.ImageField(upload_to='channels/static/channels/img', blank=True, default='static/channels/img/default.jpeg')
    channelName = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.channelName
