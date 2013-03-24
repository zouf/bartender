from django.db import models

class Ingredient(models.Model):
	name = models.CharField(max_length=500, default="Unnamed Ingredient")

class Drink(models.Model):
	name = models.CharField(max_length=500, default="Unnamed Drink")
	ingredients = models.ManyToManyField(Ingredient)
