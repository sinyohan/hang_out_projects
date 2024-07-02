from django.urls import path
from . import views

app_name = 'user_post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
