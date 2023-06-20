def nested_loop():
    n = 10
    count = 0

    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    count += 1
    return count

result = nested_loop() # n^4
print(result)

# list comprehension
squares = []
for x in range(1, 11):
    squares.append(x * x)
print(squares)

squares = [x ** 2 for x in range(1, 11)]
# 내가 원하는 것 정의하고 뒤에 내가 정의한 변수 생성 방식 정의하기
print(squares)

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)

# 문자열을 각 글자를 순회하면서 대문자로 바꾸시오
word = "hello"
upper_letters = [letter.upper() for letter in word]
print(upper_letters)

# 문자열 길이가 3 이하인 단어들만 선택하기
words = ['apple', 'banana', 'orange', 'grape', 'egg']
short_words = [word for word in words if len(word) <= 3]
print(short_words)
