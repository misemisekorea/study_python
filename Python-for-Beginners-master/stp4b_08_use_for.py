# for문
chicken = 10
for i in range(chicken):
    print('치킨 한마리 주세요.')
    print('주문 ' + str(i + 1) + ' 나왔습니다. 맛있게 드세요.')
    print()
    chicken = chicken - 1
    print('치킨이 ' + str(chicken) + '마리 남았습니다.')
