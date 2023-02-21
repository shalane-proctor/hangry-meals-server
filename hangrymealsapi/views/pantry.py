# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework import generics
from hangrymealsapi.models import Pantry, User


class PantrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pantry
        fields = ('id', 'user')
        depth = 1

class PantryView(ViewSet):

    def retrieve(self, request, pk):
        pantry = Pantry.objects.get(pk=pk)
        serializer = PantrySerializer(pantry)
        return Response(serializer.data)

    def list(self, request):
        pantries = Pantry.objects.all()
        user = request.query_params.get('user', None)
        if user is not None:
            pantries = Pantry.filter(uid=user.uid)
        serializer = PantrySerializer(pantries, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(uid=request.data["user"])
        pantry = Pantry.objects.create(
            user=user,
        )
        serializer = PantrySerializer(pantry)
        return Response(serializer.data)

    def update(self, request, pk):
        pantry = Pantry.objects.get(pk=pk)
        user = User.objects.get(uid=request.data["user"])
        pantry.user = user
        pantry.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        pantry = Pantry.objects.get(pk=pk)
        pantry.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserPantryView(generics.ListCreateAPIView):
    serializer_class = PantrySerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Pantry.objects.filter(user__id=user_id)
