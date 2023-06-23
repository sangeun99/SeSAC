import sys

from models import generateMultipleData

from models.user import User
from models.store import Store
from models.item import Item
from models.order import Order
from models.orderlist import Orderlist

import csv
from generators.order.userid import UserId
from generators.order.storeid import StoreId
from generators.orderlist.itemid import ItemId
from generators.orderlist.orderid import OrderId

from inputOutput import getUserInput, getCommandLineInput, printOps


def loadCSVFile(filename, target):
    with open(filename, newline='', encoding='UTF8') as f:
        reader = csv.reader(f)
        next(reader) ## time 빼고 읽기
        next(reader) ## header 빼고 읽기
        for row in reader:
            target.append(row)


if __name__=="__main__" :
    loadCSVFile('results/user.csv', UserId.users)
    loadCSVFile('results/store.csv', StoreId.stores)
    loadCSVFile('results/item.csv', ItemId.items)
    loadCSVFile('results/order.csv', OrderId.orders)
 
    # ===============
    #   INPUT
    # ===============

    if (len(sys.argv) > 3) :
        type, num, output = getUserInput(sys.argv)

    else :
        type, num, output = getCommandLineInput()

    # ===============
    #   GENERATE
    # ===============

    selectModel = {
        "user" : User,
        "store" : Store,
        "item" : Item,
        "order" : Order,
        "orderlist" : Orderlist
    }
    data = generateMultipleData(selectModel[type], num)

    # ===============
    #   OUTPUT
    # ===============

    printOps(type, data, output)