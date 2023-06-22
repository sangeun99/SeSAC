import random
import calendar
import datetime
import csv

# ----------------------------------------------------
#   전역 변수
# ----------------------------------------------------

# 한글 이름
firstnames = []
lastnames = []

# 주소
cities = []
gus = []
streetform = ['길', '로']

# 지점
types = []
storelocations = []

# ----------------------------------------------------
#   공통 객체 -  Address
# ----------------------------------------------------
 
class Address:
    def __init__(self) :
        global cities, gus, streetform
        city = random.choice(cities)
        gu = random.choice(gus)
        street1 = random.randint(1, 99)
        streetform = random.choice(streetform)
        street2 = random.randint(1, 99)
        self.address = f'{city} {gu} {street1}{streetform} {street2}'

    def getAddress(self):
        return self.address
    
# ----------------------------------------------------
#   User 이용 객체 - Name, Birthdate, Gender
# ----------------------------------------------------
 
class Name:
    def __init__(self) :
        global lastnames, firstnames
        self.name = random.choice(lastnames) \
                  + random.choice(firstnames)
    
    def getName(self) :
        return self.name

class Birthdate():
    def __init__(self):
        self.year = random.randint(1960, 2010)
        self.month = random.randint(1, 12)
        lastDayOfMonth = calendar.monthrange(self.year, self.month)[-1]
        self.day = random.randint(1, lastDayOfMonth+1)
    
    def getBirthdate(self):
        return f'{self.year}-{self.month:02d}-{self.day:02d}'
    
    def getAge(self):
        dateToday = datetime.datetime.now()
        age = dateToday.year - self.year + 1
        return age
    
class Gender():
    def __init__(self):
        self.gender = random.choice(['Female', 'Male'])
    
    def getGender(self) :
        return self.gender


# ----------------------------------------------------
#   Store 이용 객체 - StoreName
# ----------------------------------------------------
 

class StoreName:
    def __init__(self) :
        global types, storelocations
        self.type = random.choice(types)
        location = random.choice(storelocations)
        self.name = f'{self.type} {location}{random.randint(1,10)}호점'
    
    def getName(self) :
        return self.name
    
    def getType(self) :
        return self.type

 
# ----------------------------------------------------
#   Item 이용 객체 - StoreName
# ----------------------------------------------------

class SingleItem:

    itemTypes = {
             "Coffee": {
                "Americano": 3000,
                "Latte": 4000,
                "Espresso": 2500,
                "Cappuccino": 4500,
                "Mocha": 5000
            },
            "Juice": {
                "Orange": 2000,
                "Apple": 2500,
                "Grape": 3000,
                "Pineapple": 3500,
                "Watermelon": 4000
            },
            "Cake": {
                "Chocolate": 6000,
                "Strawberry": 5500,
                "Vanilla": 5000,
                "Red Velvet": 6500,
                "Carrot": 6000
            }
        }
    
    def __init__(self):
        typeIndex = random.randrange(len(SingleItem.itemTypes))
        self.itemType = list(SingleItem.itemTypes.keys())[typeIndex]
        itemList = list(SingleItem.itemTypes.values())[typeIndex]
        itemIndex = random.randrange(len(itemList))
        self.itemName = list(itemList.keys())[itemIndex]
        self.unitPrice = list(itemList.values())[itemIndex]

    def getItem(self):
        return self.itemType, self.itemName, self.unitPrice
    
# ----------------------------------------------------
#   객체 - User, Store, Item
# ----------------------------------------------------

class User:
    def __init__(self) :
        self.name = Name().getName()
        self.gender = Gender().getGender()
        newBirthdate = Birthdate()
        self.age = newBirthdate.getAge()
        self.birthdate = newBirthdate.getBirthdate()
        self.address = Address().getAddress()

    def getUser(self):
        return self.name, self.gender, self.age, self.birthdate, self.address

class Store:
    def __init__(self) :
        newStoreName = StoreName()
        self.name = newStoreName.getName()
        self.type = newStoreName.getType()
        self.address = Address().getAddress()

    def getStore(self):
        return self.name, self.type, self.address

class Item:
    # Name,Type,UnitPrice
    def __init__(self) :
        NewItem = SingleItem()
        self.itemName, self.itemType, self.unitPrice = NewItem.getItem()

    def getItem(self) :
        return self.itemName, self.itemType, self.unitPrice
        

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
#   각종 함수 - 데이터 생성 함수
# ----------------------------------------------------

def generateUser():
    newUser1 = User()
    return newUser1.getUser()

def generateMultipleUsers(num):
    result = []
    for _ in range(num) :
        result.append(generateUser())
    return(result)

def generateStore():
    newStore1 = Store()
    return newStore1.getStore()

def generateMultipleStores(num):
    result = []
    for _ in range(num) :
        result.append(generateStore())
    return(result)

def generateItem():
    newItem1 = Item()
    return newItem1.getItem()

def generateMultipleItems(num):
    result = []
    for _ in range(num) :
        result.append(generateItem())
    return(result)


# ----------------------------------------------------
#   메인 함수
# ----------------------------------------------------

if __name__=="__main__" :
    

    print("----------test----------------")

    for _ in range (10) :
        newItem = Item()
        print(newItem.getItem())

    print("--------------------------")
    load_files('src/firstname.txt', firstnames)
    load_files('src/lastname.txt', lastnames)
    load_files('src/cities.txt', cities)
    load_files('src/gus.txt', gus)
    load_files('src/coffeetypes.txt', types)
    load_files('src/storelocations.txt', storelocations)


    dataType = input("데이터 유형을 입력하세요 (User, Store 또는 Item): ").lower()
    dataNum = int(input("생성할 데이터 개수를 입력하세요: "))
    outputType = input("아웃풋 형태를 입력하세요 (stdout, csv, console): ")


    if dataType == "user" :
        data = generateMultipleUsers(dataNum)
    elif dataType == "store" :
        data = generateMultipleStores(dataNum)
    elif dataType == "item" :
        data = generateMultipleItems(dataNum)

    print_stdout(data)
