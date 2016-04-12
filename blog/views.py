# coding=utf-8
from django.shortcuts import render
from blog.models import Article

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list':post_list})