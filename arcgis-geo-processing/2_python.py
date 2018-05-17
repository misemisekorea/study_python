# -*- coding: utf-8 -*-
#####################
## 기본 자료형
fcName = 1
fcName = 'Road'
FCName = "Parcel"
print(fcName)
print(FCName)

#####################
## 폴더 경로 세팅
folder = "C:\\Student"
folder = r"C:\Student"
folder = "C:/Student"

fc = "Road.shp"
num = 1

fullPath = folder + "\\" + fc + "_" + str(num) #C:/Student/Road.shp_1


#####################
## 배열

fullPath = "C:/Student/Road.shp"

fcName = fullPath[11:15]#11은 포함, 15는 미포함
print(fcName)#"Road"
fcName = fullPath[:-4]
print(fcName)#C:/Student/Road

#####################
## List 자료형

fcList = ["Roads", "Streets", "Parcels", "Zipcodes"]

print fcList[0]# "Roads"

print fcList[-2] #["Roads", "Streets"]

fcList.sort()#알파벳순으로 sort
print fcList


#####################
## 가독성을 위한 줄바꿈
fcList = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
print(fcList)


#####################
## built-in functions
#built-in Exam
fields = "fields"
print len (fields)
#side pakage
import arcpy



#####################
## Accessing modules
import arcpy, os.path

fullPath = r"C:\EsriTraining\Naperville.mxd"
print os.path.basename(fullPath)#Naperville.mxd
print os.path.dirname(fullPath)#C:\EsriTraining

#####################
## 조건문 (Decision making syntax)
import arcpy, os.path, string

x = 1

if x == 1:
    print ("X is 1") #반드시 들여쓰기 해야함
elif x == 2:
    print ("X is 2")
else:
    print ("not X")

#####################
## 반복문(Looping syntax)
x = 5
while x < 10:
    print x
    x = x + 1

for x in range (1,5) :
    print x

x = [1,2,3]
for a in x:
    print(a)


#####################
## 변수 메모리에서 삭제

x = 1
print x
del x











