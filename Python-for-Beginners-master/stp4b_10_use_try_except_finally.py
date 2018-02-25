try:
    num1 = 5
    num2 = 0
    print(num1 / num2)
    print('계산끝')
except ZeroDivisionError:
    print('0으로 나누기 에러가 발생했습니다')
except (ValueError, TypeError):
    print('에러가 발생했습니다.')
except:
    print('알 수 없는 에러가 발생했습니다.')
finally:
    print('프로그램종료')
