from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context) 


def group_posts(request):
    template = 'posts/group_list.html'
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context) 

def posts_list(request):
    template = 'posts/group_list.html'
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context) 