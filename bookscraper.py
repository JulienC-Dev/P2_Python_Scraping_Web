import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/in-a-dark-dark-wood_963/index.html"

res = requests.get(url)
if res.ok:
    soup = BeautifulSoup(res.text, 'lxml')
    title = soup.find('title')
    print(title.text)
    table = soup.findAll('td')
    tds = []
    for i in table:
        tds.append(i)
    print(tds[0].get_text())
    print(tds[3].get_text())
    print(tds[2].get_text())




