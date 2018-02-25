# continue & break문
while True:
    print('누구십니까?')
    your_name = input()
    if your_name == '도깨비':
        print('안녕하세요. 도깨비님!')
    elif your_name == '저승사자':
        print('저승사자님, 또 야근이시군요!')
    elif your_name == 'pass':
        continue
        print('이 문장은 결코 출력되지 않을 겁니다.')
    elif your_name == 'exit':
        break
    else:
        print(your_name + '..., 뉘신지?')
    print()
