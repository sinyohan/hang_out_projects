# views.py in hangout directory

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
