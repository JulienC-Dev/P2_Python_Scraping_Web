import requests
from bs4 import BeautifulSoup
import csv
import bookscraper
import os


def getCategories(url):
    r = requests.get(url)
    soupi = BeautifulSoup(r.content, 'lxml')

    ## lien des catégories
    pagelist = []

    livre = soupi.find("ul", attrs={"nav nav-list"}).find("li").find('ul').findAll('li')
    for ix in livre:
        a = ix.find('a')
        path = a['href'].replace("../", "")
        url = "http://books.toscrape.com/" + path
        title = a.get_text(strip=True)

        pagelist.append((url, title))

    return pagelist

def recupimage(url):
    r = requests.get(url)
    soupi = BeautifulSoup(r.content, 'lxml')
    image = soupi.find("ol",attrs={"class": "row"}).findAll('li')
    imagetitre = []
    for imti in image:
        imgtit = imti.findAll('a')

        #Dl images
        img = imgtit[0].find('img')['src']
        print(img)
        # titres
        titres = imgtit[1]['title']
        print(titres)

        imagetitre.append(("http://books.toscrape.com/"+img, titres))

    return print(imagetitre)

if __name__ == '__main__':
    b = bookscraper.Scrap()


    urls= ("http://books.toscrape.com/index.html")
    recupimage(urls)

    # for cat in getCategories(urls):
    #
    #     with open(f'cat{cat[1]}.csv', 'w',encoding='utf-8') as p :
    #         fieldnames = ['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description',
    #                       'category', 'review_rating', 'image_url']
    #         ca = csv.DictWriter(p, fieldnames=fieldnames)
    #         ca.writeheader()
    #         for y in b.Catliv(cat[0]):
    #
    #             ca.writerow({'product_page_url': y[0], 'universal_ product_code (upc)': y[1], 'title': y[2],
    #                              'price_including_tax': y[3], 'price_excluding_tax': y[4],
    #                              'number_available': y[5], 'product_description': y[6], 'category': y[7],
    #                              'review_rating': y[8], 'image_url': y[9]})
    #
    #



    for cat in getCategories(urls):

        with open(f'cat{cat[1]}.csv', 'w',encoding='utf-8') as p :
            fieldnames = ['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description',
                          'category', 'review_rating', 'image_url']
            ca = csv.DictWriter(p, fieldnames=fieldnames)
            ca.writeheader()
            for y in b.Catliv(cat[0]):

                ca.writerow({'product_page_url': y[0], 'universal_ product_code (upc)': y[1], 'title': y[2],
                                 'price_including_tax': y[3], 'price_excluding_tax': y[4],
                                 'number_available': y[5], 'product_description': y[6], 'category': y[7],
                                 'review_rating': y[8], 'image_url': y[9]})
                # Picture_request = requests.get(y[9])
                # # with open(y[2], 'wb') as f:
                # #     f.write(Picture_request.content)





