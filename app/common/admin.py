from django.contrib import admin

from .models import *

admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(Feel)
admin.site.register(MealEntry)