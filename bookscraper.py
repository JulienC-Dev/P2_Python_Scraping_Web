import requests
from bs4 import BeautifulSoup
from bs4 import Comment

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

###

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
print("http://books.toscrape.com/catalogue/" + o[1])
###

## Récupération - UPC / Price_including_tax / Price_excluding_tax #

table = soup.findAll('tr')
tds = []
elemprod = []
for i in table:
    tds.append(i)
    for x in tds:
        elemprod = soup.findAll('th')
        elemref = soup.findAll('td')


print(elemprod[0].get_text())
print(elemref[0].get_text())

print(elemprod[3].get_text())
print(elemref[3].get_text())

print(elemprod[2].get_text())
print(elemref[2].get_text())

print(elemprod[5].get_text())
print(elemref[5].get_text())

###

'''

## Récupération - Description du produit #
prD = soup.find("div", attrs={"id":"product_description"}).find("h2")
print(prD.text)

nt = soup.find("div", attrs={"id":"product_description"}).find_next_sibling()
print(nt.get_text())

###
