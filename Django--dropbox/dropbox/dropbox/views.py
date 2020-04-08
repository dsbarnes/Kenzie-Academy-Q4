from django.shortcuts import render  # , HttpResponseRedirect, reverse
from .models import File_Object
# from .forms import

def show_tree(request):
    return render(request, 'tree.html', {'files': File_Object.objects.all()})