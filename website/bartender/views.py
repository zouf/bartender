from django.shortcuts import render
from bartender.models import Drink, Ingredient, IngredientForDrink

available_ingredients = [
	'Whiskey',
	'Vodka',
	'Tonic',
	'Soda',
	'Orange Juice',
	'Bloody Mary Mix',
	'Gin']

def bar(request):
	ingredients = Ingredient.objects.all()
	drinks = Drink.objects.filter()
	return render(
    	request,
    	'bar.html',
    	{'ingredients': ingredients,
    	'drinks': drinks})

def load(request):
	import ast

	Ingredient.objects.all().delete()
	f = open('data/ingredients.txt')
	ingredients = set(ast.literal_eval(f.read()))
	for ingredient_name in ingredients:
		i = Ingredient(name=ingredient_name)
		for available_ingredient_name in available_ingredients:
			try:
				Ingredient.objects.get(name__iexact=available_ingredient_name)
				i.is_available=True
				print available_ingredient_name
			except:
				pass
		i.save()

	Drink.objects.all().delete()
	IngredientForDrink.objects.all().delete()
	f = open('data/drinks.txt')
	drinks = ast.literal_eval(f.read())
	for drink in drinks:
		d = Drink(
			name=drink.get('name', 'Unnamed Drink'),
			category=drink.get('category'),
			rating=drink.get('rating'),
			url=drink.get('url'),
			mix_instructions=drink.get('mixingInstructions'),
			glass=drink.get('serveIn'))
		try:
			d.save()
		except:
			print 'Could not insert %s' % drink.get('name')

		for ingredient in drink.get('ingredients', []):
			ingredient_name = ingredient.get('name')
			if ingredient_name:
				i = Ingredient.objects.get(name=ingredient_name)
				ifd = IngredientForDrink(
					drink=d,
					ingredient=i,
					amount=ingredient.get('amount'))
				try:
					ifd.save()
				except:
					print 'Count not insert %s' % ingredient_name

	return render(
		request,
		'load.html',
		{})