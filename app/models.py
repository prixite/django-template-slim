from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Person(models.Model):
    name = models.CharField(max_length=128)
    tagline = models.TextField()
