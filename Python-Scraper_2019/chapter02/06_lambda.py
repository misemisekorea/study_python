#람다를 통해 속성의 개수가 2개인 태그를 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page2.html")
bsObj = BeautifulSoup(html, "html.parser")
tags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)

for tag in tags :
    print(tag)

# <div class="body" id="fakeLatin"> -> 2가지 attr을 가진 태그