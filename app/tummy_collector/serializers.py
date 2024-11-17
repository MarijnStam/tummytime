from rest_framework import serializers
from common.models import *

class FeelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feel
        fields = ['timestamp', 'feel_nr', 'symptoms']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class MealSerializer(serializers.ModelSerializer):
    
    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredient.objects.all())
    class Meta:
        model = Meal
        fields = ['meal_name', 'ingredients']
        
class MealEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = MealEntry
        fields = ['timestamp', 'name', 'ingredients']

