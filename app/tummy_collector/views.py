from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from common.models import *
from .serializers import *



def index(request):
    return HttpResponse("Some stupid shit index")

class FeelViewSet(viewsets.ModelViewSet):
    queryset = Feel.objects.all()
    serializer_class = FeelSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class MealEntryViewSet(viewsets.ModelViewSet):
    queryset = MealEntry.objects.all()
    serializer_class = MealEntrySerializer