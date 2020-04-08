from django.shortcuts import render
from .forms import Login_Form, Signup_Form
from .models import Custom_User


def index(request):
    request.user.username
    return render(request,
                  'custom_user/templates/index.html',
                  {
                    'users': Custom_User.objects.all(),
                    'first': str(type(Custom_User.objects.first()))
                  })


def login(request):
    return render(request,
                  'custom_user/templates/basic_form.html',
                  {'form': Login_Form}
                  )


def signup(request):
    return render(request,
                  'custom_user/templates/basic_form.html',
                  {'form': Signup_Form}
                  )


