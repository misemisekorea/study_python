# 외부링크에서 외부링크로 무작위 이동
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
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []

    #/로 시작하는 링크를 모두 찾습니다.
    for link in bsObj.find_all("a", href=re.compile("^(/|.*"+includeUrl+")")):
        # href속성이 존재하며
        if link.attrs['href'] is not None:
            # internalLinks에 포함되어 있지 않으며
            if link.attrs['href'] not in internalLinks:
                # /로 시작하는 도메인 + href
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


def followExternalOnly(startingSite):
    print("--------in def followExternalOnly")
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: " + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")



















