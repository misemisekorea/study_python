#형제 다루기

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

#1.img1.jpg src속성을 가지고 있는 이미지 태그
#2.이미지 태그의 부모(td)
#3.이전형제 태그
#4.태그안의 텍스트
print(bsObj.find("img", {"src" : "../img/gifts/img1.jpg"
                         }).parent.previous_sibling.get_text())

#next_siblings은 앞에서 뒤로
#previous_siblings은 뒤에서 앞으로
