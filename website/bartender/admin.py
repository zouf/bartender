from django.contrib import admin
from bartender.models import Drink, Ingredient, IngredientForDrink

admin.site.register(Drink)
admin.site.register(Ingredient)
admin.site.register(IngredientForDrink)