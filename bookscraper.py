import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/catalogue/in-a-dark-dark-wood_963/index.html"
burl = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

res = requests.get(url)
resbis = requests.get(burl)

soupbis = BeautifulSoup(resbis.text, 'lxml')
soup = BeautifulSoup(res.text, 'lxml')

links = []

## Récupération - Titre #
title = soup.find('h1')
print("Title : ")
print(title.text)


## Récupération - UPC / Price_including_tax / Price_excluding_tax #

table = soup.findAll('tr')
tds = []
elemprod = []
for i in table:
    tds.append(i)
    for x in tds:
        elemprod = soup.findAll('th')
        elemref = soup.findAll('td')

UPC = elemprod[0].get_text()

print(UPC)
print(elemref[0].get_text())

priceIncltax = elemprod[3].get_text()
print(priceIncltax)
print(elemref[3].get_text())

priceExcltax = elemprod[2].get_text()
print(priceExcltax)
print(elemref[2].get_text())

Available = elemprod[5].get_text()
print(Available)
print(elemref[5].get_text())

###

## Récupération - Description du produit #
prD = soup.find("div", attrs={"id":"product_description"}).find("h2")
prDD = prD.text
print(prDD)

nt = soup.find("div", attrs={"id":"product_description"}).find_next_sibling()
print(nt.get_text())

###






# Récupération - Product_page_url #

p = []
o = []
n = soupbis.findAll('div',attrs={"class": "image_container"})
for v in n:
    b = v.find('a')
    c = b['href']
    p = c.replace("../../../", "")
    o.append(p)

print("Product_page_url :")

urlp = ("http://books.toscrape.com/catalogue/" + o[1])
print(urlp)

####


with open('data.csv', 'w') as file:

    fieldnames = ['UPC','Titre :','priceIncltax','priceExcltax','Product_page_url :', 'Available','prDD']
    fileD = csv.DictWriter(file,fieldnames=fieldnames)
    fileD.writeheader()
    fileD.writerow({'UPC': [elemref[0].get_text()],'Titre :': [title.text],'priceIncltax' : [elemref[3].get_text()], 'priceExcltax' : [elemref[2].get_text()],'Product_page_url :': [urlp],'Available' : [elemref[5].get_text()],
                    'prDD':[nt.get_text()]})




'''
b =[]
for link in soup.find_all('a'):
    b.append(link)

print(b)

c =[]
for link in soupbis.find_all('a'):
   b = link.get('href')
   c.append(b)

print(c)
'''

'''
'''



'''
### récupération - Catégorie #
categorie = []
cat = soup.find("ul",attrs={"class":"breadcrumb"}).findAll('a')
for c in cat:
    categorie.append(c)
print("Categorie\n" + categorie[2].get_text())
###
'''
'''
### récupération - Notation #
rat = soup.find("p", attrs={"class":"instock availability"}).find_next_sibling()
rats = rat['class']
if rats[1] == "One":
    print("Review rating : \n" + "1/5")
###
'''

'''
## récupération - image url#
image = soup.find('img')
img = image['src']
print("http://books.toscrape.com/"+ img.replace("../../", ""))

##
'''
