from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Tweet
from twitteruser.models import TwitterUser
from notification.models import Notification
from .forms import Add_Tweet
from . import views


@login_required
def write_tweet(request):
    html = 'write_tweet.html'
    if request.method == "POST":
        form = Add_Tweet(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            Tweet.objects.create(
                body=data['body'],
                twitter_user=request.user
            )
            
            if '@' in data['body']:
                twitterusers = TwitterUser.objects.all()
                for usr in twitterusers:
                    if f'@{usr}' in data['body']:
                        Notification.objects.create(
                            twitteruser = TwitterUser.objects.get(username=f'{usr}'),
                            tweet = Tweet.objects.get(
                                body=data['body'], 
                                twitter_user=request.user),
                            viewed = False
                        )

        return HttpResponseRedirect(reverse('home'))

    form = Add_Tweet()
    return render(request, html, {
        'form': form,
        'notification_count': len(Notification.objects.filter(twitteruser=request.user, viewed=False)),
        'total_following': len(TwitterUser.objects.get(username=request.user).following.all()),
        'total_tweets': len(Tweet.objects.filter(twitter_user=request.user)),
        })


def single_tweet(request, id):
    if request.user.is_anonymous:
        return render(request, 'tweet.html', {'tweet': Tweet.objects.get(id=id)})

    return render(request, 'tweet.html', {
        'tweet': Tweet.objects.get(id=id),
        'notification_count': len(Notification.objects.filter(twitteruser=request.user, viewed=False)),
        'total_following': len(TwitterUser.objects.get(username=request.user).following.all()),
        'total_tweets': len(Tweet.objects.filter(twitter_user=request.user)),
        }
    )