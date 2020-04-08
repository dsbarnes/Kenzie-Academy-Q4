from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from . import views

@login_required
def notification(request):
    notifications = Notification.objects.filter(twitteruser=request.user, viewed=False)
    for n in notifications:
        n.viewed = True
        n.save()

    return render(request, 'notification.html', {
        'notifications': notifications,
        'notification_count': len(notifications),
        'total_following': len(TwitterUser.objects.get(username=request.user).following.all()),
        'total_tweets': len(Tweet.objects.filter(twitter_user=request.user))
        })