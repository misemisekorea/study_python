# 사이트에서 찾은 외부 URL을 모두 리스트로 수집
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random


pages = set()
random.seed(datetime.datetime.now())

# 페이지에서 발견된 내부 링크를 모두 목록으로 만듭니다. (뷰티풀수프객체, 도메인)
def getInternalLinks(bsObj, includeUrl):
    print("--------in def getInternalLinks")
    includeUrl = urlparse(includeUrl).schme+"://"+urlparse(includeUrl).netloc
    internalLinks = []

    #/로 시작하는 링크를 모두 찾습니다.
    for link in bsObj.find_all("a", href=re.compile("^(/|.*"+includeUrl+")")):
        # href속성이 존재하며
        if link.attrs['href'] is not None:
            # internalLinks에 포함되어 있지 않으며
            if link.attrs['href'] not in internalLinks:
                # /로 시작하면 도메인 + href
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                # /로 시작하지 않는 전체주소일 경우
                else:
                    internalLinks.append(link.attrs['href'])

    return internalLinks


# 페이지에서 발견된 외부 링크를 모두 목록으로 만듭니다.
def getExternalLinks(bsObj, excludeUrl):
    print("--------in def getExternalLinks")
    externalLinks = []
    # 현재 URL을 포함하지 않으면서 http나 www로 시작하는 링크를 모두 찾습니다.
    for link in bsObj.find_all("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        #href속성이 존재하며
        if link.attrs['href'] is not None:
            #externalLinks에 포함되어 있지 않으며
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks



def getRandomExternalLink(startingPage):
    print("--------in def getRandomExternalLink")
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]


allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    internalLinks = getInternalLinks(bsObj, urlparse(siteUrl).netloc) #http://를 제외
    externalLinks = getExternalLinks(bsObj, urlparse(siteUrl).netloc) #http://를 제외

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)

    for link in internalLinks:
        #/일 경우 -> "/"
        if link == "/":
            link = domain
        #//로 시작할 경우 -> "http:"+"//oreilly.com/test"
        elif link[0:2] == "//":
            link = "http:" + link
        #/로 시작할 경우 -> "http://oreilly.com"+"/test"
        elif link[0:1] == "/":
            link = domain + link

        if link not in allIntLinks:
            print("About to get link: " + link)
            allIntLinks.add(link)
            getAllExternalLinks(link)


domain = "http://oreilly.com"
getAllExternalLinks(domain)










