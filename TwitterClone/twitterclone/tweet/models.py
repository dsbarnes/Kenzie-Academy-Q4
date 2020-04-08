from django.db import models
from twitteruser.models import TwitterUser

# Create your models here.
class Tweet(models.Model):
    def __str__(self):
        return self.body
    
    # Need some way to know if it should display on the notifications
    # viewed_by_user = False
    
    # Confident it's this, I think there is a form widget for text area
    body = models.CharField(max_length=140)
    
    # See whichever project I had the date working
    # I think it's a form think where we set the default=date.Now() or whatever
    time_posted = models.DateTimeField(auto_now_add=True)
    
    # Also confident in this:
    # Any user can post any number of tweets,
    # but each tweet has only one user that posted it.
    twitter_user = models.ForeignKey(
        TwitterUser, on_delete=models.CASCADE)
