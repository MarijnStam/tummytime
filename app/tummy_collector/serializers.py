from rest_framework import serializers
from common.models import *

class FeelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feel
        fields = ['timestamp', 'feel_nr', 'symptoms']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['name', 'ingredients']

class MealEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealEntry
        fields = ['timestamp', 'meal', 'ingredients']

