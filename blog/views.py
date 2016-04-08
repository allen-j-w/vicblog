# coding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from blog.models import Blog


# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all().order_by('timeStamp')
    return render_to_response('index.html', {'blogs':blogs}, \
                              context_instance=RequestContext(request))