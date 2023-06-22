import csv
import datetime

from models import generateMultipleUsers, generateMultipleStores, generateMultipleItems
from models.user import User
from models.store import Store
from models.item import Item

def printStdout(data):
    for d in data:
        print(d)
    print(datetime.datetime.now())

def writeCSV(filename, header, data) :
    f = open(filename, 'w', newline='', encoding='UTF8')
    dataWriter = csv.writer(f)
    dataWriter.writerow(header)
    for d in data:
        dataWriter.writerow(d)
    createdTime = [datetime.datetime.now()]
    dataWriter.writerow(createdTime)
    f.close()

def printOps(type, num, output):
    outputDict = {
        "user" : [generateMultipleUsers(num),
                  User.header],
        "store" : [generateMultipleStores(num),
                  Store.header],
        "item" : [generateMultipleItems(num),
                  Item.header]}
    data = outputDict[type][0]
    header = outputDict[type][1]

    if output == "stdout" :
        printStdout(data)
    elif output == "csv" :
        writeCSV('result.csv', header, data)