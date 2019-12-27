from django.db import models
from random import randint
from django.contrib.auth.models import User


# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=20)
    color = models.CharField(max_length=20, default="#9999ff")
    image = models.FileField(default=None)
    rating = models.IntegerField(default=1)
    applications = models.IntegerField(default=0)

class report(models.Model):
    reporter = models.ManyToManyField(User)
    text = models.TextField(max_length=140, default=None)
