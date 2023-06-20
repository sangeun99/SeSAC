# Name,Birthdate,Gender,Address

# Jane,1990-01-03,Male,50 New York
# Jane,1990-04-14,Male,46 Philadelphia
# Jane,1981-01-07,Male,69 Los Angeles
# Emily,1975-09-03,Female,33 Philadelphia
# Olivia,1987-12-18,Male,2 Chicago
# Michael,1980-03-21,Male,18 Chicago
# Michael,1982-03-02,Male,57 Houston
# Olivia,1976-10-19,Female,36 Chicago
# Emily,1976-01-05,Female,96 New York
# John,1971-08-22,Male,76 Los Angeles
# Jane,1984-11-26,Male,7 Houston

import random
import calendar

names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']

def generate_name():
    return random.choice(names)

def generate_birthdata():
    y = random.choice(range(1950, 2000))
    m = random.choice(range(1, 13))
    lastDayOfMonth = calendar.monthrange(y, m)[-1]
    d = random.choice(range(1, lastDayOfMonth+1))
    return '{year}-{month:02d}-{day:02d}'.format(year=y, month=m, day=d)

data = []
for _ in range(10):
    name = generate_name()
    data.append(name)

for d in data:
    print(d)

print(generate_birthdata())
