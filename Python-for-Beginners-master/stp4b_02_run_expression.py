>>> 2 + 2
4
>>> 2 + 4 * 3
14
>>> (2 + 4) * 3
18
>>> (4 - 2) * ((6 + 2) / (4 - 2))
8.0
>>> 4 +
SyntaxError: invalid syntax
>>> 53 + 4 + * 2
SyntaxError: invalid syntax
>>> '도' + '깨비'
'도깨비'
>>> '깨비' + 11
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    '깨비' + 11
TypeError: Can't convert 'int' object to str implicitly
>>> '깨비' + str(11)
'깨비11'
>>> '깨비' * 5
'깨비깨비깨비깨비깨비'
