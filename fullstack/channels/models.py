from django.db import models

class Channel(models.Model):
    image = models.ImageField(upload_to='channels/static/channels/img', blank=True, default='static/channels/img/default.jpeg')
    channelName = models.CharField(max_length=255)

    def __str__(self):
        return self.channelName


