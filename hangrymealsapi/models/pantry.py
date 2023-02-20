from django.db import models
from .user import User

class Pantry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
