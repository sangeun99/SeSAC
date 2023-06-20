def find_max(numlist):
    max = int(numlist[0])
    for number in numlist :
        if max < int(number):
            max = int(number)
    return max

print("여러 개의 숫자를 입력하시오 (공백으로 구분)")
numlist = input().split()
print ("최댓값 :", find_max(numlist))