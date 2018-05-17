#실수(Floating-point)
a = 1.2
a = -3.45

a = 4.24E10#4.24*10의 10승
a = 4.24e-10#4.24*-10의 10승

#8진수
a = 0o177

#16진수
a = 0x8ff
b = 0xABC

#복소수(Complex number)
a = 1+2j
b = 3-4J

#복소수의 실수 리턴
a = 1+2j
print(a.real)#1.0

#복소수의 허수 리턴
a = 1+2j
print(a.imag)#2.0

#복소수의 켤레복소수 리턴
a = 1+2j
print(a.conjugate())#(1-2j)

#복소수의 절대값 리턴(제곱의 제곱근)
a = 1+2j
print(abs(a))#2.2360679774997898

#사칙연산
a = 3
b = 4
print(a + b)
print(a * b)
print(a / b)

#제곱
a = 3
b = 4
print(a ** b)#81

#나눗셈 후 나머지
print(7 % 3)#1
print(3 % 7)#3

#나눗셈 후 소수점 아래자리 버림
print(7 // 4)#1

