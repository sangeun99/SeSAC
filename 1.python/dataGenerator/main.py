import sys

from models import generateMultipleData

from models.user import User
from models.store import Store
from models.item import Item

from output import printOps

if __name__=="__main__" :

    if (len(sys.argv) > 3) :
        dataType = sys.argv[1].lower()
        dataNum = int(sys.argv[2])
        outputType = sys.argv[3].lower()

    else :
        dataType = input("데이터 유형을 입력하세요 (User, Store 또는 Item): ").lower()
        dataNum = int(input("생성할 데이터 개수를 입력하세요: "))
        outputType = input("아웃풋 형태를 입력하세요 (stdout, csv): ").lower()

    selectModel = {
        "user" : User,
        "store" : Store,
        "item" : Item
    }
    
    data = generateMultipleData(selectModel[dataType], dataNum)
    header = selectModel[dataType].header
    printOps(header, data, outputType)
