from django.db import models
from .user import User
from .recipe import Recipe

class Week(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monday = models.ForeignKey(Recipe, related_name='monday', on_delete=models.CASCADE)
    tuesday = models.ForeignKey(Recipe, related_name='tuesday', on_delete=models.CASCADE)
    wednesday = models.ForeignKey(
        Recipe, related_name='wednesday', on_delete=models.CASCADE)
    thursday = models.ForeignKey(
        Recipe, related_name='thursday', on_delete=models.CASCADE)
    friday = models.ForeignKey(
        Recipe, related_name='friday', on_delete=models.CASCADE)
    saturday = models.ForeignKey(Recipe, related_name='saturday', on_delete=models.CASCADE)
    sunday = models.ForeignKey(Recipe, related_name='sunday', on_delete=models.CASCADE)
    objects = models.Manager()
