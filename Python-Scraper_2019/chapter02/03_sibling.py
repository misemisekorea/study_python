#형제 다루기

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

#id가 giftList인 태그 > tr 첫번째 자식태그(테이블제목태그) > 테이블타이틀 다음 형제들
for sibling in bsObj.find("table", {"id" : "giftList"}).tr.next_siblings:
    print(sibling)

#next_siblings은 앞에서 뒤로
#previous_siblings은 뒤에서 앞으로
