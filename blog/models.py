from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


# Create your models here.
class Category(models.Model):
    """
    blog category
    """
    name = models.CharField('Category', max_length=16)


class Tag(models.Model):
    """
    blog tag
    """
    name = models.CharField('Tags', max_length=16)


class Blog(models.Model):
    """
    blogs
    """
    title = models.CharField('Title', max_length=32)
    author = models.CharField('Author', max_length=16)
    content = models.TextField('Body')
    timeStamp = models.DateTimeField('Time', auto_now_add=True)

    category = models.ForeignKey(Category, verbose_name='Category')
    tags = models.ManyToManyField(Tag, verbose_name='Tags')


class Comment(models.Model):
    """
    comments
    """
    blog = models.ForeignKey(Blog, verbose_name='Blog')

    name = models.CharField('Alias', max_length=16)
    email = models.EmailField('Email')
    comment = models.CharField('Comment', max_length=140)

    timestamp = models.DateTimeField('Time', auto_now_add=True)

admin.site.register([Category, Tag, Blog])