from django.shortcuts import render
from bartender.models import Drink, Ingredient, IngredientForDrink
from django.views.decorators.csrf import csrf_exempt
import os, operator, json                         
from django.http import HttpResponse

available_ingredients = [
	'Whiskey',
	'Vodka',
	'Tonic',
	'Soda',
	'Orange Juice',
	'Bloody Mary Mix',
	'Gin']

liquor = ['Vodka', 'Orange juice', 'Gin', 'Grenadine', 'Pineapple juice', 
	'Triple sec', 'Amaretto', 'Lemon juice', 'Tequila', 'Cranberry juice']


@csrf_exempt
def make_drink(request):
	if request.method == 'POST':
		drink_name = request.POST.get('drink_name')
		drink = Drink.objects.get(name=drink_name)

		ifds = IngredientForDrink.objects.filter(drink=drink).all()

		if len(ifds) >= 1:
			ifd = ifds[0]
			amount_text = ifd.amount.replace('oz', 'ounce')
			os.system('say %s needs %s of %s' % (ifd.drink.name, amount_text, ifd.ingredient.name))

		if len(ifds) > 1:
			for ifd in ifds[1:]:
				amount_text = ifd.amount.replace('oz', 'ounce')
				os.system('say and %s of %s' % (amount_text, ifd.ingredient.name))

	return render(request,
    	'bar.html')


@csrf_exempt
def announce(request):
	#os.system('say What drink would you like')
	return HttpResponse(json.dumps({}), mimetype="application/json")

@csrf_exempt
def order_drink(request):
	if request.method == 'POST':
		terms_heard = request.POST.get('words').split()
		print terms_heard

		possible_drinks_file = open('data/possible_drinks.txt')
		for line in possible_drinks_file.readlines():
			drink_name = line.rstrip()
			drink_terms = drink_name.split()
			for heard_term in terms_heard:
				for drink_term in drink_terms:
					if heard_term.lower() == drink_term.lower():
						os.system('say I heard you mention %s' % heard_term)
						os.system('say I can make you a %s' % drink_name)
						return HttpResponse(json.dumps({"drink": drink_name}), mimetype="application/json")

		ingredients = set()
		for heard_term in terms_heard:
			for ing in liquor:
				for ing_term in ing.split():
					if heard_term.lower() == ing_term.lower():
						ingredients.add(ing)

		if len(ingredients) > 0:
			drink_name = ' and '.join(list(ingredients))
			os.system('say I dont know what drink that is but I can make you %s' % drink_name)
			return HttpResponse(json.dumps({"drink": drink_name}), mimetype="application/json")

def bar(request):
	#os.system('say welcome to the bartender bot one point owe')
	#os.system('say please tell me the name of the drink you would like me to mix for you')

	ingredients = Ingredient.objects.all()
	drinks = Drink.objects.filter()

	# liquor = ['Vodka', 'Orange juice', 'Gin', 'Grenadine', 'Pineapple juice', 
	# 'Triple sec', 'Amaretto', 'Lemon juice', 'Tequila', 'Cranberry juice']

	# extras = ['Ice', 'Maraschino cherry', 'Cherry', 'Lemon', 'Lemon peel',
	# 	'Lemon vodka', 'Salt', 'Cherries', 'Celery salt', 'Orange vodka', 'Almond',
	# 	'Raspberry vodka', 'Pear', 'Soda water', 'Tonic water']

	# liquor = [l.lower() for l in liquor]
	# extras = [e.lower() for e in extras]

	# x = set()

	# total = 0
	# for drink in drinks:
	# 	can_serve = True
	# 	for ing in drink.ingredients.all():
	# 		if ing.name.lower() not in liquor:
	# 			if ing.name.lower() not in extras:
	# 				x.add(ing.name)
	# 				can_serve = False
	# 				break
	# 	if can_serve:
	# 		print drink
	# 		total += 1

	# print '\n %s' % total
	# print x


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