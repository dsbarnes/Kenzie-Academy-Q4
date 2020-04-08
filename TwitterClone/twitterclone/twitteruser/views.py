from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitteruser.models import TwitterUser
from notification.models import Notification
from tweet.models import Tweet


def profile(request, twitter_user):
    # Yo, I fucking one shot this line here.
    not_me = True if request.user.username != twitter_user else False
    profile = TwitterUser.objects.get(username=twitter_user)

    if request.user.is_anonymous:
        return render(request, 'profile.html', { 'profile': profile })

    return render(request, 'profile.html', {
        'profile': profile,
        'following': TwitterUser.objects.get(username=request.user).following.all(),
        'total_following': len(TwitterUser.objects.get(username=twitter_user).following.all()),
        'total_tweets': len(Tweet.objects.filter(twitter_user=profile)),
        'notification_count': len(Notification.objects.filter(twitteruser=request.user, viewed=False)),
        'not_me': not_me,
    })


@login_required
def follow(request, twitter_user):
    profile = TwitterUser.objects.get(username=twitter_user)
    current_user = TwitterUser.objects.get(username=request.user)
    current_user.following.add(profile)
    current_user.save()
    return HttpResponseRedirect(reverse('profile', args=[profile]))


@login_required
def unfollow(request, twitter_user):
    profile = TwitterUser.objects.get(username=twitter_user)
    current_user = TwitterUser.objects.get(username=request.user)
    current_user.following.remove(profile)
    current_user.save()
    return HttpResponseRedirect(reverse('profile', args=[profile]))