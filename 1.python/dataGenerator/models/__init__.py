from models.user import User
from models.store import Store
from models.item import Item

def generateUser():
    newUser1 = User()
    return newUser1.generate()

def generateMultipleUsers(num):
    result = []
    for _ in range(num) :
        result.append(generateUser())
    return(result)

def generateStore():
    newStore1 = Store()
    return newStore1.generate()

def generateMultipleStores(num):
    result = []
    for _ in range(num) :
        result.append(generateStore())
    return(result)

def generateItem():
    newItem1 = Item()
    return newItem1.generate()

def generateMultipleItems(num):
    result = []
    for _ in range(num) :
        result.append(generateItem())
    return(result)