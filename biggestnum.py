print("여러 개의 숫자를 입력하시오 (공백으로 구분)")
numlist = input().split()

max = int(numlist[0])
for number in numlist :
    if max < int(number):
        max = int(number)

print (max)