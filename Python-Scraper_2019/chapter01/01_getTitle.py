#특정 태그 가져오기
from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):

    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
        #null을 반환하거나, break 문을 실행하거나, 기타 모든 방법을 사용
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
