# while문
while True:
    print('당신은 누구십니까?')
    your_name = input()
    if your_name == '도깨비':
        print('안녕하세요. 도깨비님!')
    elif your_name == '저승사자':
        print('저승사자님, 또 야근이시군요!')
    else:
        print(your_name + '..., 뉘신지?')
    print()
