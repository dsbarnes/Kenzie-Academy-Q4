from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification


@login_required
def home(request):

    following = list(TwitterUser.objects.get(username=request.user).following.all())
    following.append(TwitterUser.objects.get(username=request.user))
    tweets = Tweet.objects.filter(twitter_user__in=following)

    return render(request, 'home.html', {
        'tweets': tweets.order_by('-time_posted'),
        'total_tweets': len(Tweet.objects.filter(twitter_user=request.user)),
        'total_following': len(following),
        'notification_count': len(Notification.objects.filter(twitteruser=request.user, viewed=False))
        })

@login_required
def redirect_home(request):
    return HttpResponseRedirect(reverse('home'))