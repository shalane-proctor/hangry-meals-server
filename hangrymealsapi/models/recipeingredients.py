from django.db import models
from .recipe import Recipe
from .ingredient import Ingredient


class RecipeIngredients(models.Model):

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    objects = models.Manager()
