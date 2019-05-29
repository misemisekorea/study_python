#html태그 중 특정 클래스 가져오기

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

"""
#타이틀 태그 전부 가져오기
nameList = bsObj.find_all({"h1","h2","h3","h4","h5","h6"})
for name in nameList:
    print(name.get_text())

#그린,레드 가져오기
nameList = bsObj.find_all("span",{"class" : {"green", "red"}})
for name in nameList:
    print(name.get_text())

#특정 텍스트 갯수 출력
nameList = bsObj.find_all(text="the prince")
print(len(nameList))

#id가 text인 태그 가져오기1
allText = bsObj.findAll(id="text")
print(allText[0].get_text())

#id가 text인 태그 가져오기2
allText = bsObj.findAll("", {"id" :"text"})
print(allText[0].get_text())

"""

#그린만 가져오기
nameList = bsObj.find_all("span",{"class" : "green"})
for name in nameList:
    print(name.get_text())

