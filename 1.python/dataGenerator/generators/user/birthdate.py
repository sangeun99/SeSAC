import calendar
import random
import datetime

class Birthdate():
    def __init__(self):
        self.year = random.randint(1960, 2010)
        self.month = random.randint(1, 12)
        lastDayOfMonth = calendar.monthrange(self.year, self.month)[-1]
        self.day = random.randint(1, lastDayOfMonth+1)
    
    def generate(self):
        return f'{self.year}-{self.month:02d}-{self.day:02d}'
    
    def generateAge(self):
        dateToday = datetime.datetime.now()
        age = dateToday.year - self.year + 1
        return age