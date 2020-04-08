from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Post
from .forms import Add_Post


def index(request):
    return render(request,
                  'ghostpost/index.html',
                  {'posts': Post.objects.all()})


def up_vote(request, pk):
    post = Post.objects.get(pk=pk)
    post.up_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('index'))


def down_vote(request, pk):
    post = Post.objects.get(pk=pk)
    post.down_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('index'))


def up_votes_ascending(request):
    return(render(request,
                  'ghostpost/index.html',
                  {'posts': Post.objects.order_by('-up_votes')}))


def up_votes_descending(request):
    return(render(request,
                  'ghostpost/index.html',
                  {'posts': Post.objects.order_by('up_votes')}))


def down_votes_ascending(request):
    return(render(request,
                  'ghostpost/index.html',
                  {'posts': Post.objects.order_by('-down_votes')}))


def down_votes_descending(request):
    return(render(request,
                  'ghostpost/index.html',
                  {'posts': Post.objects.order_by('down_votes')}))


def boasts_only(request):
    return(render(request,
                  'ghostpost/index.html',
                  {'posts': Post.objects.filter(is_boast=True)}))


def roasts_only(request):
    return(render(request,
                  'ghostpost/index.html',
                  {'posts': Post.objects.filter(is_boast=False)}))


def most_recent(request):
    return(render(request,
                      'ghostpost/index.html',
                      {'posts': Post.objects.order_by('submission_time')}))


def add_post(request):
    html = 'ghostpost/simple_form.html'
    if request.method == "POST":
        form = Add_Post(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                is_boast=data['is_boast'],
                contents=data['contents'],
                up_votes=0,
                down_votes=0
            )
        return HttpResponseRedirect(reverse("index"))

    form = Add_Post()
    return render(request, html, {'form': form})


