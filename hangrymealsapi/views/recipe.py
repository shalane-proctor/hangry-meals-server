# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework import generics
from hangrymealsapi.models import Recipe, User

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'user', 'name', 'instructions')
        depth = 1


class RecipeView(ViewSet):

    def retrieve(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def list(self, request):
        recipes = Recipe.objects.all()
        user = request.query_params.get('user', None)
        if user is not None:
            recipes = recipes.filter(uid=user.uid)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(uid=request.data["user"])
        recipe = Recipe.objects.create(
            user=user,
            name=request.data["name"],
            instructions=request.data["instructions"],
        )
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def update(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        user = User.objects.get(uid=request.data["user"])
        Recipe.user = user
        Recipe.name = request.data["name"]
        Recipe.instructions = request.data["instructions"]
        recipe.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserRecipeView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Recipe.objects.filter(user__id=user_id)
