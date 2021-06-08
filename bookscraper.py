import requests
from bs4 import BeautifulSoup
import csv



class Scrap:
    ## Scraping sur un livre

    def getbookinfo (self,url):

        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'lxml')


        # Récupération - Product_page_url #
        print("Product_page_url :")
        b = (url)
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



        if soup.find("div", attrs={"id": "product_description"}) is None:
            nt = "Pas de description du livre"
            print(nt)
        else:
            nt = soup.find("div", attrs={"id": "product_description"}).find_next_sibling()
            nt = nt.get_text()
            print(nt)



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

        return ([b,elemref[0].get_text(), title.text, elemref[3].get_text(),
                                     elemref[2].get_text(),
                                    elemref[5].get_text(),nt, cate, ratnote, imgs])



    # scroll toutes les pages d'une categorie et recupere les liens de chaque livres
    def Catliv(self,burl):


        resbis = requests.get(burl)
        soupbis = BeautifulSoup(resbis.content, 'lxml')

        b = soupbis.find('li', attrs={"class": "next"})
        pages = []
        c = []

        if b is not None:
            for page in range(1, 10):
                    page = burl.replace("index.html", (f'page-{page}.html'))
                    r = requests.get(page)

                    if r.status_code != 200:
                        break
                    pages.append(page)
                    pg = requests.get(page)
                    souppage = BeautifulSoup(pg.content, 'lxml')
                    pp = souppage.findAll('li', attrs={"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
                    for link in pp:

                        li = link.find('a')['href'].replace("../../../", "")
                        c.append("http://books.toscrape.com/catalogue/" + li)

        else:
            p = soupbis.findAll('li', attrs={"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
            for link in p:
                pg = link.find('a')['href'].replace("../../../", "")
                c.append("http://books.toscrape.com/catalogue/" + pg)


        listcat= []
        for a in c:
            listcat.append(self.getbookinfo(a))


        return listcat




if __name__ == '__main__':

    cats = Scrap()

    cats.getbookinfo("http://books.toscrape.com/catalogue/alice-in-wonderland-alices-adventures-in-wonderland-1_5/index.html")

    burl = "http://books.toscrape.com/catalogue/category/books/classics_6/index.html"
    bp = cats.Catliv(burl)

    # récupération Data d'une catégorie dans un fichier CSV
    with open('datacatlivres.csv', 'w', encoding='utf-8') as w:
        fieldnames = ['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax',
                      'price_excluding_tax', 'number_available', 'product_description',
                      'category', 'review_rating', 'image_url']

        catw = csv.DictWriter(w, fieldnames=fieldnames)
        catw.writeheader()
        for i in bp:
            catw.writerow({'product_page_url': i[0],'universal_ product_code (upc)': i[1],'title': i[2],'price_including_tax': i[3],'price_excluding_tax': i[4],
                 'number_available': i[5],'product_description': i[6],'category': i[7],'review_rating': i[8],'image_url': i[9]})



