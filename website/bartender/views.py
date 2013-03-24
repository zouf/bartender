from django.shortcuts import render
from bartender.models import Drink, Ingredient

def bar(request):
	ingredients = Ingredient.objects.all()
	drinks = Drink.objects.all()
	return render(
    	request,
    	'bar.html',
    	{'ingredients': ingredients,
    	'drinks': drinks})

def load(request):
	Ingredient.objects.all().delete()
	gin = Ingredient(name="Gin")
	gin.save()
	tonic = Ingredient(name="Tonic")
	tonic.save()
	vodka = Ingredient(name="Vodka")
	vodka.save()

	Drink.objects.all().delete()
	d = Drink(name="Gin & Tonic")
	d.save()
	d.ingredients.add(gin)
	d.ingredients.add(tonic)
	d.save()
	return render(
		request,
		'load.html',
		{})