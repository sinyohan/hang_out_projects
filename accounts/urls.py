# urls.py in accounts directory

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
]
