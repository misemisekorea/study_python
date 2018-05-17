#List
a = []
b = [1,2,3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', "is"]
e = [1,2, ['Life', 'is']]
print("{0}, {1}, {2}, {3}, {4}".format(a,b,c,d,e))


print("=" * 50)
print("{0:=^50}".format("Indexing"))
print("=" * 50)


#Indexing
a = [1,2,3]
print(a[0])#1
print(a[0]+a[2])#4
print(a[-1])#3

#이중 리스트
a = [1,2,3, ['a','b','c']]
print(a[-1])#['a','b','c']
print(a[-1][0])#a
print(a[-1][1])#b
print(a[-1][2])#c

#삼중 리스트
a = [1,2,3, ['a','b',['Life', 'is']]]
print(a[-1])#['a','b',['Life', 'is']]
print(a[-1][2])#['Life','is']
print(a[-1][2][0])#Life


print("=" * 50)
print("{0:=^50}".format("Slicing"))
print("=" * 50)


#Slicing
a = [1,2,3,4,5]
print(a[0:2])
b = a[:2]
c = a[2:]
print(b)
print(c)

#중첩 리스트 Slicing
a = [1,2,3,['a','b','c'],4,5]
print(a[2:5])#[3, ['a', 'b', 'c'], 4]
print(a[3][:2])#['a', 'b']


print("=" * 50)
print("{0:=^50}".format("리스트 연산자"))
print("=" * 50)


#리스트 연산자
#리스트 더하기(+)
a = [1,2,3]
b = [4,5,6]
print(a+b)#[1, 2, 3, 4, 5, 6]

#리스트 반복(*)
a = [1,2,3]
print(a*3)#[1, 2, 3, 1, 2, 3, 1, 2, 3]

#리스트 수정
a = [1,2,3]
a[2] = 4
print(a)#[1, 2, 4]

a = [1,2,3]
a[1] = ['a','b','c']
print(a)#[1, ['a', 'b', 'c'], 3]

a = [1,2,3]
a[1:2] = ['a','b','c']
print(a)#[1, 'a', 'b', 'c', 3]


#리스트 삭제 1
a = [1,2,3,4,5,6]
a[1:3] = []
print(a)#[1, 4, 5, 6]

#리스트 삭제 2
a = [1,2,3,4,5,6]
del a[1]
print(a)#[1, 3, 4, 5, 6]


print("=" * 50)
print("{0:=^50}".format("리스트 관련 함수들"))
print("=" * 50)


#리스트 관련 함수들
#리스트 요소 추가(append)
a = [1,2,3]
a.append(4)
print(a)#[1, 2, 3, 4]

a = [1,2,3,4]
a.append([5,6])
print(a)#[1, 2, 3, 4,[5, 6]]

#리스트 정렬
a = [1,4,3,2]
a.sort()
print(a)#[1,2,3,4]

a = ['a','c','b']
a.sort()
print(a)#['a', 'b', 'c']

#리스트 뒤집기(reverse)
a = ['a','c','b']
a.reverse()
print(a)#['b', 'c', 'a']

#리스트 위치 반환(index) -> 값이 존재하지 않으면 오류발생
a = [1,2,3]
print(a.index(3))#2 -> a[2]

a = ['a','b','c']
print(a.index('b'))#1 -> a[1]

#리스트에 요소 삽입(insert)
a = [1,2,3]
a.insert(0,4)#a[0]위치에 4삽입
print(a)#[4, 1, 2, 3]

a = [1,2,3,4]
a.insert(3,5)#a[3]위치에 5삽입
print(a)#[1, 2, 3, 5, 4]

#리스트 요소 제거
a = [1,2,3,1,2,3]
a.remove(3)#숫자3을 제거
print(a)#[1, 2, 1, 2, 3]
a.remove(3)#숫자3을 한번 더 제거
print(a)#[1, 2, 1, 2]

#리스트 요소 끄집어내기(pop) -> 맨 마지막 요소를 돌려주고 그 요소는 삭제
a = [1,2,3]
print(a.pop())#3
print(a)#[1,2]

a = [1,2,3]
print(a.pop(1))#2
print(a)#[1,3]

#리스트에 포함된 요소 x의 개수 세기(count)
a = [1,2,3,1]
print(a.count(1))#2 -> 숫자1은 2개


#리스트 확장(extend)
a = [1,2,3]
a.extend([4,5])
print(a)#[1, 2, 3, 4, 5]

a += [6,7]
print(a)#[1, 2, 3, 4, 5, 6, 7]

b = [8,9]
a.extend(b)
print(a)#[1, 2, 3, 4, 5, 6, 7, 8, 9]