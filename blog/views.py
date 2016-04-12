# coding=utf-8
from django.http import Http404
from django.shortcuts import render, redirect
from blog.models import Article


# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list':post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post':post})


def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list':post_list, 'error':False})


def about_me(request):
    return render(request, 'aboutme.html')


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list':post_list})


def search_blog(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            post_list = Article.objects.all()
            return render(request, 'home.html', {'post_list':post_list})
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list':post_list, 'error':True})
            else:
                return render(request, 'archives.html', {'post_list':post_list, 'error':False})
    return redirect('/')