from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# --------------- Feel Model ------------------ #
# --------------------------------------------- #       
class Feel(models.Model):
    feel = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"{self.timestamp} - {self.feel}"
    
# ------------ Ingredient Model --------------- #
# --------------------------------------------- #    
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

# ---------------- Meal Model ----------------- #
# --------------------------------------------- #
class Meal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ingredients = models.ManyToManyField(Ingredient)
    
    def __str__(self):
        return self.name
    
# ------------- MealEntry Model --------------- #
# --------------------------------------------- #   
class MealEntry(models.Model):
    timestamp = models.DateTimeField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    
    def __str__(self):
        return f"{self.timestamp} - {self.meal.name}"
    