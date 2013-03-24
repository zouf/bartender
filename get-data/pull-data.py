#!/usr/bin/python
from bs4 import BeautifulSoup, SoupStrainer
import httplib2
import re
import pprint
import json
from datetime import datetime

AllIngredients = []
AllDrinks = []


def pull_site(siteurl):
  http = httplib2.Http()
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Encoding': 'none',
         'Accept-Language': 'en-US,en;q=0.8',
         'Connection': 'keep-alive'}
  status, response = http.request(siteurl,headers=hdr)
  
  
  theDrink = dict()
  
  soup = BeautifulSoup(response)
  drinkName = soup.h1.get_text()
  theDrink['name'] = drinkName
  uls = soup.findAll("a","ingr")

  category = soup.find(text=re.compile('Category:')).parent.parent.parent.find('td').find('small').get_text()
  serveIn = soup.find(text=re.compile('Serve in:')).parent.parent.parent.find('td').find('small').get_text()
  rating = soup.find(text=re.compile('Rating:')).parent.parent.parent.find('td').find('small').get_text()
  mixingInstructions = soup.find(text=re.compile('Mixing instructions:')).parent.parent.find('p').get_text()

  
  theDrink['url'] = siteurl
  theDrink['category'] = category
  theDrink['serveIn'] = serveIn
  theDrink['rating'] = rating
  theDrink['mixingInstructions'] = mixingInstructions
  
  theDrink['ingredients'] = []
  for link in  uls:
    ingr = dict()
    ingrName = link.get_text()
    
    ingr['name'] = ingrName
    #ridiculous hack since this website doesnt format its lists properly. Or beautifulsoup doesnt read them properly
    parentText = link.parent.get_text().split(ingrName)
    amount = parentText[0]
    
    ingr['amount'] = amount
    AllIngredients.append(ingrName)
    
    theDrink['ingredients'].append(ingr)
  AllDrinks.append(theDrink)
    
    
       
def dumpData():
  fp = open('AllDrinks.json','w')
  json.dump(AllDrinks,fp)
  fp = open('AllIngredients.json','w')
  json.dump(AllIngredients,fp)


def main():
  i = 1
  #this is what the website has for now
  NUM_DRINKS = 6218 
  
  for i in xrange(1,NUM_DRINKS+1):
    try:
      pull_site("http://www.webtender.com/db/drink/"+str(i))  
      
      if i %100 == 0:
        print 'At Drink ' + str(i)
        dumpData()
    except Exception as e:
      print 'Exception at ' + str(i)
      dumpData()
      pass
      
  print 'We are done. We have ' + str(len(AllDrinks)) + ' drinks. \n\nException:' + str(e)
  dumpData()

if __name__ == "__main__":
  main()
