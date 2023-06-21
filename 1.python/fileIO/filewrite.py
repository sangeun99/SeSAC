data = "Hello World!\n"
with open("names.txt", "a") as file:
    file.write(data)

print("파일 쓰기 완료!")