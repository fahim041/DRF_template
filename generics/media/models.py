from django.db import models
from django.db.models.base import Model
from comment.models import Comment
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.News
