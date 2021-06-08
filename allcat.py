import requests
from bs4 import BeautifulSoup
import csv
import bookscraper

# affiche les liens de chaque catégories
def allcat(urls):

        r = requests.get(urls)
        soupi = BeautifulSoup(r.content,'lxml')

        ## lien des catégories
        pagelist =[]

        pagecat = soupi.find("ul",  attrs={"nav nav-list"}).findAll('a')
        for ix in pagecat:
            rt = ix['href'].replace("../", "")

            pagelist.append("http://books.toscrape.com/" + rt)
        return (pagelist[1 :len(pagelist)-1])

#affiche les noms de chaque catégories
def affichecatte(urls):
    rr = requests.get(urls)
    soupii = BeautifulSoup(rr.content, 'lxml')

    ppp = []
    seeka = soupii.find("ul", attrs={"nav nav-list"}).find('li').find('ul').findAll('a')
    for i in seeka:
        ppp.append(i.get_text(strip=True))
    return ppp


b = bookscraper.Scrap()
'''
burl = "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html"

bp = b.Catliv(burl)
'''

urls= ("http://books.toscrape.com/index.html")


print(affichecatte(urls))

print(allcat(urls))



for i in affichecatte(urls):
    print(i)
    with open(f'cat{i}.csv', 'w',encoding='utf-8') as p:
        fieldnames = ['product_page_url', 'UPC', 'Titre :', 'priceIncltax', 'priceExcltax', 'Available', 'prDD',
                      'Cattitre', 'rattitre', 'imgtitre']
        ca = csv.DictWriter(p, fieldnames=fieldnames)
        ca.writeheader()
        for x in allcat(urls):

            print(x)
            burl = x

            for y in b.Catliv(burl):
                print(y)
                if
                ca.writerow({'product_page_url': y[0], 'UPC': y[1], 'Titre :': y[2], 'priceIncltax': y[3], 'priceExcltax': y[4],
                         'Available': y[5], 'prDD': y[6], 'Cattitre': y[7], 'rattitre': y[8], 'imgtitre': y[9]})

