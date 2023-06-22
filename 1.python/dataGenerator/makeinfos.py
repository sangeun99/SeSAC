import random
import calendar
import csv

def load_data():
    return load_firstnames(), load_lastnames(), load_cities()

def load_firstnames():
    names = []
    f = open('firstname.txt', 'r', encoding='UTF8')
    for line in f.readlines() :
        names.append(line.strip())  
    f.close
    return names

def load_lastnames():
    names = []
    f = open('lastname.txt', 'r', encoding='UTF8')
    for line in f.readlines() :
        names.append(line.strip())  
    f.close
    return names

def load_cities():
    cities = []
    f = open('cities.txt', 'r', encoding='UTF8')
    for line in f.readlines() :
        cities.append(line.strip())  
    f.close
    return cities

def generate_name(firstnames, lastnames):
    fn = random.choice(firstnames)
    ln = random.choice(lastnames)
    return ln + fn

def generate_birthdate():
    year = random.randrange(1950, 2000)
    month = random.randrange(1, 13)
    lastDayOfMonth = calendar.monthrange(year, month)[-1]
    day = random.randrange(1, lastDayOfMonth+1)
    return f'{year}-{month:02d}-{day:02d}'

def generate_gender():
    return random.choice(['Female', 'Male'])

def generate_address(cities):
    city = random.choice(cities)
    gu = random.choice(['강서구', '중구', '서구', '남구'])
    street1 = random.randrange(1, 100)
    street = random.choice(['길', '로'])
    street2 = random.randrange(1, 100)
    return f'{city} {gu} {street1}{street} {street2}'


def generate_info(number):
    data = []
    for _ in range(number):
        name = generate_name(firstnames, lastnames)
        birthdate = generate_birthdate()
        gender = generate_gender()
        address = generate_address(cities)
        info = [name, birthdate, gender, address]
        data.append(info)
    return data

def write_csv(data) :
    f = open('infos.csv', 'w', newline='', encoding='UTF8')
    wr = csv.writer(f)
    header = ['Name', 'Birthdate', 'Gender', 'Address']
    wr.writerow(header)
    for d in data:
        wr.writerow(d)
    f.close()

def print_console(data):
    for d in data:
        print(d)

firstnames, lastnames, cities = load_data()
data = generate_info(30)
write_csv(data)
print_console(data)
