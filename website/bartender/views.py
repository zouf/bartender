from django.shortcuts import render
from bartender.models import Drink, Ingredient, IngredientForDrink
from django.views.decorators.csrf import csrf_exempt
import os, operator                           

available_ingredients = [
	'Whiskey',
	'Vodka',
	'Tonic',
	'Soda',
	'Orange Juice',
	'Bloody Mary Mix',
	'Gin']

@csrf_exempt
def order_drink(request):
	if request.method == 'POST':
		terms_heard = request.POST.get('words')

		drink = None
		if 'margarita' in terms_heard:
			drink = 'margarita'
		if 'gin' in terms_heard:
			drink = 'gin and tonic'

		if drink:
			os.system('say I think you asked me for a %s' % drink)
	return render(
    	request,
    	'bar.html')

def bar(request):
	ingredients = Ingredient.objects.all()
	drinks = Drink.objects.filter()

	liquor = ['Vodka', 'Orange juice', 'Gin', 'Grenadine', 'Pineapple juice', 
	'Triple sec', 'Amaretto', 'Lemon juice', 'Tequila', 'Cranberry juice']

	extras = ['Ice', 'Maraschino cherry', 'Cherry', 'Lemon', 'Lemon peel',
		'Lemon vodka', 'Salt', 'Cherries', 'Celery salt', 'Orange vodka', 'Almond',
		'Raspberry vodka', 'Pear',
	 'Soda water', 'Tonic water']

	liquor = [l.lower() for l in liquor]
	extras = [e.lower() for e in extras]

	x = set()

	total = 0
	for drink in drinks:
		can_serve = True
		for ing in drink.ingredients.all():
			if ing.name.lower() not in liquor:
				if ing.name.lower() not in extras:
					x.add(ing.name)
					can_serve = False
					break
		if can_serve:
			print drink,'|',
			total += 1

	print '\n %s' % total
	print x


	# freq = {}
	# for drink in drinks:
	# 	for ing in drink.ingredients.all():
	# 		freq[ing] = freq.get(ing, 0) + 1

	# from operator import itemgetter
	# for a,b in sorted(freq.iteritems(), key=itemgetter(1), reverse=True)[:50]:
	# 	print a,b

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