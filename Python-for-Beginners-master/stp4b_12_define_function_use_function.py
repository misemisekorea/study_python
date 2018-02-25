# define function
def exchange_money(exchange_to, krw):
    # 나라별 환율 정보
    rates = [('usd', 1196.50), ('jpy', 10.2629), ('eur', 1262.85), ('cny', 175.06)]

    for rate in rates:
        if exchange_to == rate[0]:
            amount = krw / rate[1]
            print(exchange_to.upper() + ' 환율은 ' + str(rate[1]) + '입니다.')
            print(str(krw) + ' KRW를 환전한 결과는 ' + str(amount) + ' ' + exchange_to.upper() + '입니다.')
            print()
            break
    return

# use function
exchange_money('usd', 100000)
exchange_money('jpy', 100000)
exchange_money('eur', 100000)
exchange_money('cny', 100000)
