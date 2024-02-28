from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'feel', FeelViewSet)
router.register(r'ingredient', IngredientViewSet)
router.register(r'meal', MealViewSet)
router.register(r'meal_entry', MealEntryViewSet)

urlpatterns = [
	path('', include(router.urls)),
]