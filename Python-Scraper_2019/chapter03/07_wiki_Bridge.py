from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
random.seed(datetime.datetime.now())

#bodyContent div태그 밑에 a태그이면서 :이 포함되어 있지 않고 /wiki/로 시작
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.find("div", {"id" : "bodyContent"}).find_all("a",
                            href=re.compile("^(/wiki/)((?!:).)*$")) :
        if 'href' in link.attrs:
            print(link.attrs['href'])


links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)