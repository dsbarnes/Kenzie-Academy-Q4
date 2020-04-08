from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from twitteruser.models import TwitterUser
from .forms import Login_Form, Signup_Form


def login_user(request):
    html = 'login_user.html'
    if request.method == 'POST':
        form = Login_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))

    form = Login_Form()
    return render(request, html, {'form': form})


def sign_up(request):
    html = 'sign_up.html'
    if request.method == 'POST':
        form = Signup_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create(
                username=data['username'],
                display_name=data['display_name'],
                password=data['password'],
            )
            new_user.save()

        return HttpResponseRedirect(reverse('login_user'))

    form = Signup_Form()
    return render(request, html, {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')