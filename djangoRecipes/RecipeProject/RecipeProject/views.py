from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Author, Recipe
from .forms import Add_Author, Add_Recipe, Login_Form, Signup_Form


def index(request):
    return render(request,
                  'RecipeProject/index.html',
                  {'recipes': Recipe.objects.all()}
                  )


def author(request, author):
    return render(request,
                  'RecipeProject/author.html',
                  {'authors': Author.objects.get(name=author),
                   'recipes': Recipe.objects.filter(author__name=author)
                   }
                  )


def detail(request, recipe):
    return render(request,
                  'RecipeProject/detail.html',
                  {'recipes': Recipe.objects.get(title=recipe)}
                  )


#@user_passes_test(lambda user: user.is_staff)
@staff_member_required()
def add_author(request):
    html = 'RecipeProject/generic_form.html'
    if request.method == "POST":
        form = Add_Author(request.POST)
        # ALWAYS
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
        return HttpResponseRedirect(reverse("index"))

    form = Add_Author()
    return render(request, html, {'form': form})


@login_required()
def add_recipe(request):
    html = 'RecipeProject/generic_form.html'
    if request.method == "POST":
        form = Add_Recipe(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                time_required=data['time_required'],
                instructions=data['instructions']
            )
        return HttpResponseRedirect(reverse("index"))

    form = Add_Recipe()
    return render(request, html, {'form': form})


def signup_user(request):
    html = 'RecipeProject/generic_form.html'
    if request.method == 'POST':
        form = Signup_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['name'],
                None,
                data['password'],
            )
            # user.save()
            login(request, user)
            # This author creation is Petes code from demo:
            Author.objects.create(
                name=data['name'],
                user=user
            )
            return HttpResponseRedirect(reverse('index'))

    form = Signup_Form()
    return render(request, html, {'form': form})


def login_user(request):
    html = 'RecipeProject/generic_form.html'
    if request.method == 'POST':
        form = Login_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))

    form = Login_Form()
    return render(request, html, {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
