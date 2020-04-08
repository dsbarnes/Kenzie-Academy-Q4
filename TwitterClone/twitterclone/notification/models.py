
from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet

# Create your models here.
class Notification(models.Model):
    def __str__(self):
        return self.twitteruser.username

    twitteruser = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    viewed = models.BooleanField()