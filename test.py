# 튜플 (a, b)
def get_name_and_age() :
    return "John", 25

name, age = get_name_and_age()
print(name, age)

# 리스트 - 배열 [] 형태로 관리
shopping_list=["apple", "banana", "orange"]
print(shopping_list)
shopping_list.append("grape")
print(shopping_list)
shopping_list.remove("banana")
print(shopping_list)

# 딕셔너리
# key-value
student = {
    "name" : "John",
    "age" : 25,
    "university" : "abcUNI"
    }

print("Name : ", student['name'])
print("Age : ", student['age'])
print("University : ", student['university'])

numbers = [1, 2, 3, 4, 5]
for num in numbers :
    if (num % 2 == 0) :
        print(num)


# 홀수 리스트와 짝수 리스트를 따로 만들어서 목록에 추가하시오
# even_numbers, odd_numbers

even_numbers = []
odd_numbers = []
for num in numbers :
    if (num % 2 == 0) :
        even_numbers.append(num)
    else :
        odd_numbers.append(num)

print(even_numbers)
print(odd_numbers)