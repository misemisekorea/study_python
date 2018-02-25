# 파일 쓰기
file = open("newfile.txt", "w")
file.write("Python is powerful... and fast;")
file.close()

# 파일 읽기
file = open("newfile.txt", "r")
print(file.read())
file.close()
