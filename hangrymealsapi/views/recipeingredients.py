# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework import generics
from hangrymealsapi.models import RecipeIngredients, Recipe, Ingredient



class RecipeIngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredients
        fields = ('id', 'recipe', 'ingredient')
        depth = 2


class RecipeIngredientsView(ViewSet):

    def retrieve(self, request, pk):
        recipeingredients = RecipeIngredients.objects.get(pk=pk)
        serializer = RecipeIngredientsSerializer(recipeingredients)
        return Response(serializer.data)

    def list(self, request):
        recipeingredients = RecipeIngredients.objects.all()
        recipe = request.query_params.get('recipe', None)
        if recipe is not None:
            recipe = recipeingredients.filter(recipe=recipe.id)
        ingredient = request.query_params.get('ingredient', None)
        if ingredient is not None:
            ingredient = recipeingredients.filter(ingredient=ingredient.id)
        serializer = RecipeIngredientsSerializer(recipeingredients, many=True)
        return Response(serializer.data)

    def create(self, request):
        recipe = Recipe.objects.get(pk=request.data["recipe"])
        ingredient = Ingredient.objects.get(pk=request.data["ingredient"])
        recipeingredients = RecipeIngredients.objects.create(
            recipe=recipe,
            ingredient=ingredient,
        )
        serializer = RecipeIngredientsSerializer(recipeingredients)
        return Response(serializer.data)

    def update(self, request, pk):
        recipeingredients = RecipeIngredients.objects.get(pk=pk)
        recipe = Recipe.objects.get(pk=request.data["recipe"])
        ingredient = Ingredient.objects.get(pk=request.data["ingredient"])
        recipeingredients.recipe = recipe
        recipeingredients.ingredient = ingredient
        recipeingredients.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        recipeingredients = RecipeIngredients.objects.get(pk=pk)
        recipeingredients.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ByRecipeIngredientsView(generics.ListCreateAPIView):
    serializer_class = RecipeIngredientsSerializer

    def get_queryset(self):
        ingredient_id = self.kwargs['ingredient_id']
        return RecipeIngredients.objects.filter(ingredient__id=ingredient_id)
