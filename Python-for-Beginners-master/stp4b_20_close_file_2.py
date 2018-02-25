# 파일 쓰기
with open("filename.txt", "w") as f:
    f.write("This is an amazing and beautiful story for you.")

# 파일 읽기
with open("filename.txt") as f:
    print(f.read())
