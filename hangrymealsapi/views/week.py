# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework import generics
from hangrymealsapi.models import Week, User, Recipe


class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = ('id', 'user', 'monday', 'tuesday',
                  'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
        depth = 2


class WeekView(ViewSet):

    def retrieve(self, request, pk):
        week = Week.objects.get(pk=pk)
        serializer = WeekSerializer(week)
        return Response(serializer.data)

    def list(self, request):
        weeks = Week.objects.all()
        user = request.query_params.get('user', None)
        if user is not None:
            weeks = weeks.filter(uid=user.uid)
        recipe = request.query_params.get('recipe', None)
        if recipe is not None:
            recipe = Week.filter(recipe=recipe.id)
        serializer = WeekSerializer(weeks, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(uid=request.data["user"])
        monday = Recipe.objects.get(pk=request.data["monday"])
        tuesday = Recipe.objects.get(pk=request.data["tuesday"])
        wednesday = Recipe.objects.get(pk=request.data["wednesday"])
        thursday = Recipe.objects.get(pk=request.data["thursday"])
        friday = Recipe.objects.get(pk=request.data["friday"])
        saturday = Recipe.objects.get(pk=request.data["saturday"])
        sunday = Recipe.objects.get(pk=request.data["sunday"])
        week = Week.objects.create(
            user=user,
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
            sunday=sunday,
        )
        serializer = WeekSerializer(week)
        return Response(serializer.data)

    def update(self, request, pk):
        week = Week.objects.get(pk=pk)
        user = User.objects.get(uid=request.data["user"])
        monday = Recipe.objects.get(pk=request.data["monday"])
        tuesday = Recipe.objects.get(pk=request.data["tuesday"])
        wednesday = Recipe.objects.get(pk=request.data["wednesday"])
        thursday = Recipe.objects.get(pk=request.data["thursday"])
        friday = Recipe.objects.get(pk=request.data["friday"])
        saturday = Recipe.objects.get(pk=request.data["saturday"])
        sunday = Recipe.objects.get(pk=request.data["sunday"])
        week.user = user
        week.monday = monday
        week.tuesday = tuesday
        week.wednesday = wednesday
        week.thursday = thursday
        week.friday = friday
        week.saturday = saturday
        week.sunday = sunday
        week.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        week = Week.objects.get(pk=pk)
        week.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserWeekView(generics.ListCreateAPIView):
    serializer_class = WeekSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Week.objects.filter(user__id=user_id)
