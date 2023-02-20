# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework import generics
from hangrymealsapi.models import Ingredient, User


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'user', 'in_stock')
        depth = 1


class IngredientView(ViewSet):

    def retrieve(self, request, pk):
        ingredient = Ingredient.objects.get(pk=pk)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    def list(self, request):
        ingredients = Ingredient.objects.all()
        user = request.query_params.get('user', None)
        if user is not None:
            ingredients = Ingredient.filter(uid=user.uid)
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(uid=request.data["user"])
        ingredient = Ingredient.objects.create(
            user=user,
            name=request.data["name"],
            in_stock=request.data["in_stock"],
        )
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    def update(self, request, pk):
        ingredient = Ingredient.objects.get(pk=pk)
        user = User.objects.get(uid=request.data["user"])
        ingredient.user = user
        ingredient.name = request.data["name"]
        ingredient.in_stock = request.data["in_stock"]
        ingredient.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        ingredient = Ingredient.objects.get(pk=pk)
        ingredient.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserIngredientView(generics.ListCreateAPIView):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Ingredient.objects.filter(user__id=user_id)
