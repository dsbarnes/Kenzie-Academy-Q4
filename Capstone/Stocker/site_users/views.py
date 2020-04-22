from django.views import View

from django.shortcuts import redirect
from django.shortcuts import render, HttpResponseRedirect, reverse

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.urls import path

from django.conf import settings
from portfolio.models import Portfolio, Holdings, Company
from .models import Custom_User
from .forms import Login_Form, Signup_Form, Deposit_Form, Withdraw_Form, Search_Form
from .helpers import *
import requests


def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)


@login_required(login_url="/login/")
def index(request):

    follow_list = request.user.favorites.split(',')[1:]
    follow_data = multiFetcher(follow_list)
    company_data = [fetchCompanyData(tkr) for tkr in follow_list]
    search_form = Search_Form(request.POST)

    if request.method == "POST":
        if search_form.is_valid():
            data = search_form.cleaned_data
            ticker = data['ticker']
            stock_data = fetchTicker(ticker)
            return render(request, 'index.html',
                        {
                            'form': search_form,
                            'data': stock_data,
                            'following': follow_data,
                            'company': company_data
                        })

    return render(request, 'index.html',
                    {
                        'form': search_form,
                        'following': follow_data,
                        'company': company_data,
                        'portfolio': request.user.portfolio.stocks.all(),
                        'balance': request.user.deposits
                    })


class Profile_view(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html',
            {
                'user': request.user,
                'deposit_form': Deposit_Form(),
                'withdraw_form': Withdraw_Form()
            }
        )

    def post(self, request, *args, **kwargs):
        deposit_form = Deposit_Form(request.POST)
        withdraw_form = Withdraw_Form(request.POST)

        def do_form_stuff(f):
            form = f
            return form.cleaned_data

        if deposit_form.is_valid() or withdraw_form.is_valid():

            if deposit_form.is_valid():
                amount = do_form_stuff(deposit_form)['deposit']
                request.user.deposits += amount
                request.user.save()

            elif withdraw_form.is_valid():
                amount = do_form_stuff(withdraw_form)['withdraw']
                request.user.withdraws -= amount
                request.user.save()

            else:
                return 'Should not be able to get here'

        return render(request, 'profile.html',
                    {
                        'user': request.user,
                        'deposit_form': deposit_form,
                        'withdraw_form': withdraw_form
                    })


@login_required(login_url="/login/")
def add_to_following(request, company):

    request.user.favorites += f',{company}'
    request.user.save()
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url="/login/")
def buy(request, company):
    data = fetchTicker(company)
    return render(request, 'buy.html', {'data': data})


@login_required(login_url="/login/")
def sell(request, company):
    data = fetchTicker(company)
    return render(request, 'sell.html', {'data': data})


@login_required(login_url="/login/")
def finish_buy(request, ticker, amount):

    data = fetchTicker(ticker)
    co = Company.objects.get(ticker_symbol=ticker)

    if not request.user.portfolio.stocks.filter(stock=co):
        ho = Holdings.objects.create(stock=co, count=int(amount))
        request.user.portfolio.stocks.add(ho)

    else:
        stock_to_update = request.user.portfolio.stocks.filter(stock=co).first()
        stock_to_update.count += int(amount)
        stock_to_update.save()

    return HttpResponseRedirect(reverse('index'))


@login_required(login_url="/login/")
def finish_sell(request, ticker, amount):

    data = fetchTicker(ticker)
    co = Company.objects.get(ticker_symbol=ticker)

    try:
        stock_to_update = request.user.portfolio.stocks.filter(stock=co).first()
        if stock_to_update.count >= amount:
            stock_to_update.count -= int(amount)
            stock_to_update.save()
        else:
            print('error')
    except:
        print('idk')

    return HttpResponseRedirect(reverse('index'))

class LoginView(View):
    html = 'basic_form.html'
    form_class = Login_Form

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.html, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if request.method == "POST":
            form = Login_Form(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                user = authenticate(username=data['username'], password=data['password'])
                login(request, user)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect("/")
                else:
                    return HttpResponseRedirect("login/")
        return render(request, self.html, {'form': form})

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def signup(request):
    html = 'sign_up_form.html'

    if request.method == 'POST':
        form = Signup_Form(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = Custom_User.objects.create_user(
                email=data['email'],
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=data['password'],
            )
            Portfolio.objects.create(
                name='',
                owner=user
            )
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = Signup_Form()
    return render(request, html, {'form': form})
