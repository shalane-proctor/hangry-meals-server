"""hangrymeals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework import routers
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from hangrymealsapi.views import check_user, register_user, UserView, IngredientView, UserIngredientView, PantryView, UserPantryView, PantryIngredientsView, RecipeIngredientsView, RecipeView, UserRecipeView, WeekView, UserWeekView, ByRecipeIngredientsView, AllPantryIngredientsView, InPantryIngredientView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', UserView, 'user')
router.register(r'ingredient', IngredientView, 'ingredient')
router.register(r'pantry', PantryView, 'pantry')
router.register(r'pantryingredient', PantryIngredientsView, 'pantryingredient')
router.register(r'recipeingredients', RecipeIngredientsView, 'recipeingredients')
router.register(r'recipe', RecipeView, 'recipe')
router.register(r'week', WeekView, 'week')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('user-ingredient/<int:user_id>/',
         UserIngredientView.as_view(), name='user'),

    path('user-pantry/<int:user_id>',
         UserPantryView.as_view(), name='user'),

    path('user-recipe/<int:user_id>/',
         UserRecipeView.as_view(), name='user'),

    path('user-week/<int:user_id>/',
         UserWeekView.as_view(), name='user'),

    path('recipe-ingredients/<int:recipe_id>/',
         ByRecipeIngredientsView.as_view(), name='recipe'),
    path('pantry-ingredients/<int:pantry_id>/',
         AllPantryIngredientsView.as_view(), name='pantry'),
    path('single-pantry-ingredients/<int:ingredient_id>/',
         InPantryIngredientView.as_view(), name='ingredient'),
]
