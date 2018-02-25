>>> list1 = ['도깨비', '저승사자', 939]
>>> list1
['도깨비', '저승사자', 939]
>>> list1[0]
'도깨비'
>>> list1[1]
'저승사자'
>>> list1[2]
939
>>> list1.append('김신')
>>> list1
['도깨비', '저승사자', 939, '김신']
>>> list1.remove('김신')
>>> list1
['도깨비', '저승사자', 939]
>>> del list1[2]
>>> list1
['도깨비', '저승사자']
>>> list1.insert(1, '김신')
>>> list1
['도깨비', '김신', '저승사자']
>>> list1.insert(3, '왕여')
>>> list1
['도깨비', '김신', '저승사자', '왕여']
>>> list1.sort()
>>> list1
['김신', '도깨비', '왕여', '저승사자']
>>> list1.reverse()
>>> list1
['저승사자', '왕여', '도깨비', '김신']
>>> tuple1 = ('도깨비', '김신')
>>> tuple1
('도깨비', '김신')
>>> tuple1.append('저승사자')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    tuple1.append('저승사자')
AttributeError: 'tuple' object has no attribute 'append'