from django.db import models
from datetime import datetime

class Podcast(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    source = models.CharField(max_length=255, default="")
    audio = models.CharField(max_length=255, default="")
    image = models.CharField(max_length=255, default="")
    episode_title = models.CharField(max_length=255, default="")
    numLikes = models.IntegerField(default=0)
    numDislikes = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def like(self):
        self.numLikes += 1

    def dislike(self):
        self.numDislikes += 1
