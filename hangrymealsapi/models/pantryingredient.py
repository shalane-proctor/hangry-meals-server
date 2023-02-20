from django.db import models
from .pantry import Pantry
from .ingredient import Ingredient

class PantryIngredient(models.Model):
    pantry = models.ForeignKey(Pantry, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    objects = models.Manager()
