# views.py in accounts directory

from django.shortcuts import render

def signup(request):
    return render(request, 'accounts/signup.html')

def home(request):
    return render(request, 'accounts/home.html')
