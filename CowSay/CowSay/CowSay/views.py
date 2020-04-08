from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import admin
from .models import Cow_Model
from .forms import Cow_Say_Form
import subprocess

admin.site.register(Cow_Model)

def home(request):
    html = 'index.html'
    
    if request.method == 'POST':
        form = Cow_Say_Form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cow_shit = subprocess.check_output(
                ['cowsay', data['cow_says']])
            
            Cow_Model.objects.create(
              cow_says = cow_shit
            )
        return HttpResponseRedirect(reverse('home'))

    form = Cow_Say_Form()
    return render(request, 'index.html',
        {'form': form, 
        'cow_says': Cow_Model.objects.all().order_by('-pk')[:1]})

def history(request):
    return render(request, 'history.html',
        {'cow_shit': Cow_Model.objects.all().order_by("-pk")[:10]})