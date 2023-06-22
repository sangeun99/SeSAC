import csv
import datetime

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

def printOps(header, data, output):
    if output == "stdout" :
        printStdout(data)
    elif output == "csv" :
        writeCSV('result.csv', header, data)