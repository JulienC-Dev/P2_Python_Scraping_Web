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

        return ([b,elemref[0].get_text(), title.text, elemref[3].get_text(),
                                     elemref[2].get_text(),
                                    elemref[5].get_text(),
                                    nt.get_text(), cate, ratnote, imgs])

    def __init__(self, b):
        self.b = b



    ###


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

        listcat =[]
        for a in c:
            listcat.append(self.getbookinfo(a))

        return print(listcat)

site = Scrap()
site.Catliv("http://books.toscrape.com/catalogue/category/books/mystery_3/index.html")

'''
print(re)

tl = []
tl.append(re)
print(tl)
'''
'''
    with open('datacatlivres.csv', 'w', encoding='utf-8') as w:
        fieldnames = ['product_page_url', 'UPC', 'Titre :', 'priceIncltax', 'priceExcltax', 'Available', 'prDD',
                      'Cattitre', 'rattitre', 'imgtitre']

        catw = csv.DictWriter(w, fieldnames=fieldnames)
        catw.writeheader()
        catw.writerows({'Product_page_url :': [b], 'UPC': [elemref[0].get_text()], 'Titre :': [title.text],
                                    'priceIncltax': [elemref[3].get_text()], 'priceExcltax': [elemref[2].get_text()],
                                    'Available': [elemref[5].get_text()],
                                    'prDD': [nt.get_text()], 'Cattitre': [cate], 'rattitre': [ratnote], 'imgtitre': imgs})

    '''
# récupération Data dans un fichier CSV

'''
with open('data.csv', 'r', encoding='utf-8') as f :
    tl = []
    fileD = csv.reader(f)
    for row in fileD:
        tl.append(re)

    with open('datacatlivres.csv', 'w', encoding='utf-8') as w :
        fieldnames = ['product_page_url', 'UPC', 'Titre :', 'priceIncltax', 'priceExcltax', 'Available', 'prDD',
                      'Cattitre', 'rattitre', 'imgtitre']

        catw = csv.DictWriter(w, fieldnames=fieldnames)
        catw.writeheader()
        for r in fieldnames:
            catw.writerow({'product_page_url': , 'UPC': tl, 'Titre :': tl, 'priceIncltax': tl, 'priceExcltax':tl, 'Available':tl, 'prDD':tl,
                          'Cattitre':tl, 'rattitre':tl, 'imgtitre':tl})
'''




'''
'''
'''
                # récupération Data dans un fichier CSV

                fieldnames = ['product_page_url', 'UPC', 'Titre :', 'priceIncltax', 'priceExcltax', 'Available', 'prDD',
                              'Cattitre', 'rattitre', 'imgtitre']

                
                fileD = csv.DictWriter(file, fieldnames=fieldnames)
                fileD.writeheader()
                
                
                fileD = csv.writer(file,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                fileD.writerow(fieldnames)
                fileD.writerow([b,elemref[0].get_text(), title.text, elemref[3].get_text(),
                                 elemref[2].get_text(),
                                elemref[5].get_text(),
                                nt.get_text(), cate, ratnote, imgs])
                ##
                
                
                
                fileD.writerow({'Product_page_url :': [b], UPC: [elemref[0].get_text()], 'Titre :': [title.text],
                                priceIncltax: [elemref[3].get_text()], priceExcltax: [elemref[2].get_text()],
                                Available: [elemref[5].get_text()],
                                prDD: [nt.get_text()], Cattitre: [cate], rattitre: [ratnote], imgtitre: imgs})
                
        ##contrôle d'une deuxième page sur une catégorie
        if soupbis.find("ul", attrs={"class": "pager"}).find('li', attrs={"class": "next"}):
            pass
        else:
            break   
   '''
'''
'''
'''
## lien des catégories 
pagelist =[]
pagecat = soupbis.find("ul",  attrs={"nav nav-list"}).findAll('a')
for ix in pagecat:
    rt = ix['href'].replace("../", "")
    pagelist.append("http://books.toscrape.com/catalogue/category/books/" + rt)

print(pagelist[1 :len(pagelist)-1])


'''
'''
marche mais passable
tl = []
tl.append(re)
print(tl)

with open('datacatlivres.csv', 'w', encoding='utf-8') as w:
        catw = csv.writer(w,delimiter=',', quotechar=' ', dialect='excel')
        catw.writerow(['product_page_url', 'UPC', 'Titre :', 'priceIncltax', 'priceExcltax', 'Available', 'prDD',
                       'Cattitre', 'rattitre', 'imgtitre'])

        catw.writerow(tl)
'''