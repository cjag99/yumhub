from django.contrib import admin
from django.apps import AppConfig
from .models import Author, Category, Ingredient, Recipe, RecipeIngredient

# Register your models here.
class ApirestfulConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'APIRESTful'
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)