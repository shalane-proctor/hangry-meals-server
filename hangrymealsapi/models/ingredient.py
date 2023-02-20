from django.db import models
from .user import User

class Ingredient(models.Model):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    in_stock = models.BooleanField(default=False)
    objects = models.Manager()
