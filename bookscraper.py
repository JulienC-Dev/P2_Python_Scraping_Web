import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/catalogue/in-a-dark-dark-wood_963/index.html"
burl = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

res = requests.get(url)
resbis = requests.get(burl)

soupbis = BeautifulSoup(resbis.text, 'lxml')
soup = BeautifulSoup(res.text, 'lxml')


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


### récupération - Catégorie #
categorie = []
cat = soup.find("ul",attrs={"class":"breadcrumb"}).findAll('a')
for c in cat:
    categorie.append(c)
Cattitre = "Categorie"
cate = categorie[2].get_text()
print(cate)
###

### récupération - Notation #
rat = soup.find("p", attrs={"class":"instock availability"}).find_next_sibling()
rats = rat['class']
rattitre = "Review rating :"
if rats[1] == "One":
    ratnote = "1/5"
    print("Review rating : \n" + ratnote)


###


## récupération - image url#
image = soup.find('img')
img = image['src']
imgs = "http://books.toscrape.com/"+ img.replace("../../", "")
imgtitre = "image url"
print(imgs)

##
'''
## création fichier CSV scraper sur une page livre
with open('data.csv', 'w', encoding='utf-8') as file:

    fieldnames = ['Product_page_url :',UPC,'Titre :',priceIncltax,priceExcltax, Available,prDD, Cattitre, rattitre, imgtitre]
    fileD = csv.DictWriter(file,fieldnames=fieldnames)
    fileD.writeheader()
    fileD.writerow({'Product_page_url :': [urlp],UPC: [elemref[0].get_text()],'Titre :': [title.text],priceIncltax : [elemref[3].get_text()], priceExcltax : [elemref[2].get_text()],Available : [elemref[5].get_text()],
                    prDD:[nt.get_text()], Cattitre: [cate], rattitre : [ratnote], imgtitre : imgs})

####
'''

c =[]
links = soupbis.findAll('div', attrs={"class":"image_container"})
for link in links:
    li = link.find('a')['href'].replace("../../../", "")
    c.append("http://books.toscrape.com/catalogue/"+ li)

print(c)

