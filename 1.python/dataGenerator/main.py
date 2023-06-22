import sys

from output import printOps

if __name__=="__main__" :

    print("----------test------------")
    print("--------------------------")
    if (len(sys.argv) > 3) :
        dataType = sys.argv[1].lower()
        dataNum = int(sys.argv[2])
        outputType = sys.argv[3].lower()

    else :
        dataType = input("데이터 유형을 입력하세요 (User, Store 또는 Item): ").lower()
        dataNum = int(input("생성할 데이터 개수를 입력하세요: "))
        outputType = input("아웃풋 형태를 입력하세요 (stdout, csv): ").lower()

    printOps(dataType, dataNum, outputType)