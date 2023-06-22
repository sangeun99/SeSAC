import csv

from generators.common.address import Address
from generators.user.name import Name
from generators.store.storename import StoreName

from models import generateMultipleUsers, generateMultipleStores, generateMultipleItems

# ----------------------------------------------------
#   각종 함수 - 데이터 불러오기 및 내보내기
# ----------------------------------------------------

def load_files(filename, target):
    try :
        f = open(filename, 'r', encoding='UTF8')
        for line in f.readlines() :
            target.append(line.strip())  
        f.close
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

def write_csv(filename, data) :
    f = open(filename, 'w', newline='', encoding='UTF8')
    wr = csv.writer(f)
    header = ['Name', 'Birthdate', 'Gender', 'Address']
    wr.writerow(header)
    for d in data:
        wr.writerow(d)
    f.close()

def print_stdout(data):
    for d in data:
        print(d)

# ----------------------------------------------------
#   메인 함수
# ----------------------------------------------------

if __name__=="__main__" :

    # print("----------test----------------")
    # for _ in range (3) :
    #     newItem = Item()
    #     print(newItem.generate())
    # print("--------------------------")

    load_files('src/firstname.txt', Name.firstnames)
    load_files('src/lastname.txt', Name.lastnames)
    load_files('src/cities.txt', Address.cities)
    load_files('src/gus.txt', Address.gus)
    load_files('src/coffeetypes.txt', StoreName.types)
    load_files('src/storelocations.txt', StoreName.storelocations)

    dataType = input("데이터 유형을 입력하세요 (User, Store 또는 Item): ").lower()
    dataNum = int(input("생성할 데이터 개수를 입력하세요: "))
    outputType = input("아웃풋 형태를 입력하세요 (stdout, csv, console): ").lower()

    if dataType == "user" :
        data = generateMultipleUsers(dataNum)
    elif dataType == "store" :
        data = generateMultipleStores(dataNum)
    elif dataType == "item" :
        data = generateMultipleItems(dataNum)

    print_stdout(data)