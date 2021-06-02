import requests
from bs4 import BeautifulSoup
import csv



linkss = []

with open('data.csv', 'w', encoding='utf-8') as file:

    for x in range(1,3):
        burl = (f'http://books.toscrape.com/catalogue/category/books/mystery_3/page-{x}.html')
        resbis = requests.get(burl)
        soupbis = BeautifulSoup(resbis.text, 'lxml')


        linkss.append(burl)

        ### selection des blocs livres dans une catégorie

        links = soupbis.findAll('div', attrs={"class": "image_container"})

        for link in links:
            c = []
            li = link.find('a')['href'].replace("../../../", "")
            c.append("http://books.toscrape.com/catalogue/" + li)

            ## Scraping sur chaque livres
            for livre in c:
                url = livre
                res = requests.get(url)
                soup = BeautifulSoup(res.text, 'lxml')

                # Récupération - Product_page_url #
                print("Product_page_url :")
                b = ("http://books.toscrape.com/catalogue/" + li)
                print(b)
                ##

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
                if rats[1] == "Two":
                    ratnote = "2/5"
                    print("Review rating : \n" + ratnote)
                if rats[1] == "Three":
                    ratnote = "3/5"
                    print("Review rating : \n" + ratnote)
                if rats[1] == "Four":
                    ratnote = "4/5"
                    print("Review rating : \n" + ratnote)
                if rats[1] == "Five":
                    ratnote = "5/5"
                    print("Review rating : \n" + ratnote)
                ###

                ## récupération - image url#
                image = soup.find('img')
                img = image['src']
                imgs = "http://books.toscrape.com/"+ img.replace("../../", "")
                imgtitre = "image url"
                print(imgs)

                # récupération Data dans un fichier CSV

                fieldnames = ['Product_page_url :', UPC, 'Titre :', priceIncltax, priceExcltax, Available, prDD,
                              Cattitre, rattitre, imgtitre]
                fileD = csv.DictWriter(file, fieldnames=fieldnames)
                fileD.writeheader()
                fileD.writerow({'Product_page_url :': [b], UPC: [elemref[0].get_text()], 'Titre :': [title.text],
                                priceIncltax: [elemref[3].get_text()], priceExcltax: [elemref[2].get_text()],
                                Available: [elemref[5].get_text()],
                                prDD: [nt.get_text()], Cattitre: [cate], rattitre: [ratnote], imgtitre: imgs})
                ##

        ##contrôle d'une deuxième page sur une catégorie
        if soupbis.find("ul", attrs={"class": "pager"}).find('li', attrs={"class": "next"}):
            pass
        else:
            break

'''
## lien des catégories 
pagelist =[]
pagecat = soupbis.find("ul",  attrs={"nav nav-list"}).findAll('a')
for ix in pagecat:
    rt = ix['href'].replace("../", "")
    pagelist.append("http://books.toscrape.com/catalogue/category/books/" + rt)

print(pagelist[1 :len(pagelist)-1])
'''