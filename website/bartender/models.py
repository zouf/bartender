from django.db import models

class Ingredient(models.Model):
	name = models.CharField(max_length=500, default="Unnamed Ingredient")
	is_available = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Drink(models.Model):
	name = models.CharField(max_length=1000, default="Unnamed Drink")
	category = models.CharField(max_length=1000, null=True)
	rating = models.CharField(max_length=1000, null=True)
	url = models.CharField(max_length=1000, null=True)
	mix_instructions = models.TextField(null=True)
	glass = models.CharField(max_length=1000, null=True)

	ingredients = models.ManyToManyField(Ingredient, through='IngredientForDrink')

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['name']


class IngredientForDrink(models.Model):
	drink = models.ForeignKey(Drink)
	ingredient = models.ForeignKey(Ingredient)
	amount = models.CharField(max_length=500, null=True)

	def __unicode__(self):
		return '%s needs %s of %s' % (self.drink.name, self.amount, self.ingredient.name)