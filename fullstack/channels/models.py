from django.db import models

class Channel(models.Model):
    image = models.ImageField(upload_to='channels/static/channels/img', blank=True, default='static/channels/img/9WBG5tw.jpeg')
    channelName = models.CharField(max_length=255)
    created_date = models.DateField(auto_now_add=True)
    article_title = models.CharField(max_length=100)
    article_description = models.TextField()

    def __str__(self):
        return self.channelName
