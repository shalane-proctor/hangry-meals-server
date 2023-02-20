from django.db import models
from .user import User

class Recipe(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    instructions = models.CharField(max_length=1000)
    objects = models.Manager()
