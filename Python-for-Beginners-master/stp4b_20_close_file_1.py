try:
    file = open("filename.txt")
    print(file.read())

finally:
    file.close()
