from django.db import models
from channels.models import Channel
from django.contrib.auth.models import User

class Article(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=100)
    article_description = models.TextField()
    article_created_date = models.DateField(auto_now_add=True)
    creators = models.ManyToManyField(User, related_name='created_articles')

    def __str__(self):
        return self.article_title
