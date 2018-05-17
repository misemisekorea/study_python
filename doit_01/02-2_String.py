print("Hello World")
print('Python is fun')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')

#작은 따옴표 포함
food = "Python's favorite food is perl"
print(food)

#큰 따옴표 포함
say = '"Python is very easy." he says.'
print(say)

#\(백슬래시)를 이용하여 문자열 포함
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
print(food)
print(say)


#여러줄 작성
multiline = "Life is too short\nYou need python"
print(multiline)

numtiline = '''
Life is too short
You need python
'''
print(multiline)


numtiline = """
Life is too short
You need python
"""
print(multiline)


#문자열 연산
head = "Python"
tail = "is fun!"
print(head+tail)

#문자열 곱하기
a = "python"
print(a*2)

#문자열 응용
print("=" * 50)
print("My Program")
print("=" * 50)


#Indexing String
a = "Life if too short, You need Python"
print(a[3])
print(a[12])
print(a[-1])
print(a[-0])#1번째
print(a[-2])#뒤에서 2번째
print(a[-5])#뒤에서 5번째

#Slicing String
a = "Life is too short, You need Python"
print(a[0:4])#0<=a<4
print(a[0:2])#Li
print(a[5:7])#is
print(a[12:17])#short
print(a[19:])#You need Python
print(a[:17])#Life is too short
print(a[:])#Life is too short, You need Python


print("=" * 50)

#weather 1
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

#weather 2
a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)

#문자열 교체
a = "Pithon"
print(a[:1])
print(a[2:])
print(a[:1] + 'y' + a[2:])


print("=" * 50)


#formating String
#Number
print("I eat %d apples" % 3)

#String
print("I eat %s apples" % "five")

#변수 활용 1
number = 3
print("I eat %d apples" % number)

#변수 활용 2
number =10
day = "three"
print("I ate %d apples. so I was sick for %s days." %(number, day))

#변수 활용 3 %s
print("I have %s apples" % 3)
print("I have %s apples" % "three")
print("I have %s apples" % 3.234)

#%문자 사용
print("%d%%" % 98)#98%


#정렬과 공백
#오른쪽 정렬
print("%10s" % "hi")#'        hi'
#왼쪽 정렬
print("%-10sjane" % "hi")#'hi        jane'

#소수점 표현
print("%0.4f" % 3.42134234)#'3.4213'

print("%10.4f" % 3.42134234)#문자열 공간 10개에서 4자리 표시 '    3.4213'


print("="*50)

#문자 개수 세기(count)
a = "hobby"
print(a.count('b'))
print(a.__len__())

#문자 위치찾기 1(find)
a = "Python is best choice"
print(a.find("b"))#10
print(a.find("f"))#-1 존재x

#문자 위치찾기 2(index) -> 값이 존재하지 않으면 오류발생
a = "Life is too short"
print(a.index('t'))#8
#print(a.index('k'))#오류발생

#문자열 삽입(join)
a = ","
print(a.join('abcd'))#a,b,c,d

#소문자 -> 대문자 (upper)
a = "hi"
print(a.upper())

#대문자 -> 소문자 (lower)
a = "HI"
print(a.lower())

#왼쪽 공백 지우기(lstrip)
a = " hi "
print(a.lstrip())

#오른쪽 공백 지우기(rstrip)
a = " hi "
print(a.rstrip())

#양쪽 공백 지우기(strip)
a = " hi "
print(a.strip())


print("="*50)


#문자열 바꾸기(replace)
a = "Life is too short"
b = a.replace("Life", "Your leg")
print(b)

#문자열 나누기
a = "Life is too short"
print(a.split())#공백을 기준으로 문자열 나눔

a = "a:b:c:d"
print(a.split(":"))


print("=" * 50)
print("=" * 50)


#고급 문자열 포매팅
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))

number = 3
print("I eat {0} apples".format(number))

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

#이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days".format(number="seven", day=3))

#인덱스와 이름 혼용
print("I ate {0} apples. so was sick for {day} days".format("six",day=4))

#왼쪽 정렬
print("{0:<10}".format("hi"))#'hi        '

#오른쪽 정렬
print("{0:>10}".format("hi"))#'        hi'

#가운데 정렬
print("{0:^10}".format("hi"))#'    hi    '

#공백 채우기
print("{0:=^10}".format("hi"))#====hi====
print("{0:!<10}".format("hi"))#hi!!!!!!!!

#소수점으로 표현
print("{0:0.4f}".format(3.42134234))#3.4213
print("{0:10.4f}".format(3.42134234))#'    3.4213'

#'{' 또는 '}' 문자 표현
print("{{and}}".format())