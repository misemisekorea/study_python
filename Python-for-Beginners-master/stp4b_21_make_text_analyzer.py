# 전체 텍스트에서 특정 문자의 갯수를 카운트하는 함수
def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

# 파일명을 입력받기
file = input("파일을 선택하세요: ")

# 입력받은 파일을 열어서 파일 내용 읽기
with open(file) as f:
    text = f.read()
print(text)

# a에서 z까지 각 알파벳이 파일 내용에 사용되는 비율 계산하기
for char in "abcdefghijklmnopqrstuvwxyz":
    percent = 100 * count_char(text, char) / len(text)
    print("{0} - {1}".format(char, round(percent, 2)))
