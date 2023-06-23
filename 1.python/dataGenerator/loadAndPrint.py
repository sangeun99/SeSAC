import csv
import datetime

def getUserInput(arguments):
    try : 
        dataType = arguments[1].lower()
        dataNum = int(arguments[2])
        outputType = arguments[3].lower()
    except ValueError:
        print("실행이 종료됩니다. 'python main.py User 10 csv'와 같은 형식으로 실행하세요")
        exit(1)
    return dataType, dataNum, outputType

def getCommandLineInput():
    try:
        dataType = input("데이터 유형을 입력하세요 (User, Store 또는 Item): ").lower()
        dataNum = int(input("생성할 데이터 개수를 입력하세요: "))
        outputType = input("아웃풋 형태를 입력하세요 (stdout, csv): ").lower()

    except ValueError:
        print("처음부터 다시 입력해주세요.")
        dataType, dataNum, outputType = getCommandLineInput()
    return dataType, dataNum, outputType

def printStdout(data) :
    for d in data:
        print(d.values())
    print(datetime.datetime.now())

def writeCSV(filename, data) :
    f = open(filename, 'w', newline='', encoding='UTF8')
    dataWriter = csv.writer(f)
    dataWriter.writerow(data[0].keys())
    for d in data:
        dataWriter.writerow(d.values())
    createdTime = [datetime.datetime.now()]
    dataWriter.writerow(createdTime)
    f.close()

def printOps(filename, data, output) :
    if output == 'stdout' :
        printStdout(data)
    elif output == 'csv' :
        writeCSV(f'results/{filename}.csv', data)