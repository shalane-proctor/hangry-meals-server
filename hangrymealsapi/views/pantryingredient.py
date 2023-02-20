# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework import generics
from hangrymealsapi.models import PantryIngredient, Pantry, Ingredient


class PantryIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantryIngredient
        fields = ('id', 'pantry', 'ingredient')
        depth = 2


class PantryIngredientsView(ViewSet):

    def retrieve(self, request, pk):
        pantryingredient = PantryIngredient.objects.get(pk=pk)
        serializer = PantryIngredientSerializer(pantryingredient)
        return Response(serializer.data)

    def list(self, request):
        pantryingredient= PantryIngredient.objects.all()
        pantry = request.query_params.get('pantry', None)
        if pantry is not None:
            pantry = PantryIngredient.filter(pantry=pantry.id)
        ingredient = request.query_params.get('ingredient', None)
        if ingredient is not None:
            ingredient = PantryIngredient.filter(ingredient=ingredient.id)
        serializer = PantryIngredientSerializer(pantryingredient, many=True)
        return Response(serializer.data)

    def create(self, request):
        pantry = Pantry.objects.get(pk=request.data["pantry"])
        ingredient = Ingredient.objects.get(pk=request.data["ingredient"])
        pantryingredient = PantryIngredient.objects.create(
            pantry=pantry,
            ingredient=ingredient,
        )
        serializer = PantryIngredientSerializer(pantryingredient)
        return Response(serializer.data)

    def update(self, request, pk):
        pantryingredients = PantryIngredient.objects.get(pk=pk)
        pantry = Pantry.objects.get(pk=request.data["pantry"])
        ingredient = Ingredient.objects.get(pk=request.data["ingredient"])
        pantryingredients.Pantry = pantry
        pantryingredients.ingredient = ingredient
        pantryingredients.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        pantryingredient = PantryIngredient.objects.get(pk=pk)
        pantryingredient.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
