print("여러개의 숫자를 입력하시오 (공백으로 구분)")
numlist = map(int, input().split())

max = numlist[0]
for number in numlist :
    if max < number:
        max = number

print (max)