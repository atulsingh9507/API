from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet,RatingViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')
router.register(r'ratings', RatingViewSet, basename='rating')

urlpatterns = [
    path('', include(router.urls)),  # Include all routes from the router
]
