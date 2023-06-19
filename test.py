# 1: 구구단 출력하기

for num in range(2, 10):
    print("{}단".format(num))
    for i in range (1, 10) :
        print("{} x {} = {}".format(num, i, num*i))
    print("\n")

