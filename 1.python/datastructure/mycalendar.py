#import calendar

#def print_calendar(year, month):
#    print(calendar.month(year, month))

## 사용자로부터 연도와 월 입력 받기
#year = int(input("연도를 입력하세요: "))
#month = int(input("월을 입력하세요: "))

## 달력 출력
#print_calendar(year, month)

dayOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def print_calendar(year, month) :

    print()

# 0년 1월 1일은 일요일


year = int(input("연도를 입력하세요: "))
month = int(input("월을 입력하세요: "))

print_calendar(year, month)