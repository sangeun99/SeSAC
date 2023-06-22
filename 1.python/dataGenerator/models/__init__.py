from models.user import User
from models.store import Store
from models.item import Item


def generateMultipleData(dataType, num) :
    result = []
    for _ in range(num):
        newData = dataType().generate()
        result.append(newData)
    return(result)