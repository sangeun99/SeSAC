def find_max(numlist):
    if len(numlist) == 0 :
        return -1
    max = numlist[0]
    for number in numlist :
        if max < number:
            max = number
    return max


data1 = [1, 55, 123, 5]
print("data1 최댓값 :", find_max(data1))

numlist = input("여러 개의 숫자를 입력하시오: ").split()
print ("최댓값 :", find_max(numlist))

numlist2 = list(map(int, input().split()))
text = input()
numlist3 = [int(text) for text in text.split()]