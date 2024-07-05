from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'user_post/post_list.html', {'posts': posts})
def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})