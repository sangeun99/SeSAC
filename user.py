users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
]

def find_users(name) :
    result = []
    for user in users :
        if user['name'] == name :
            result.append(user) 
            
print(find_users('Alice'))

def find_users_age(name, age) :
    result = []
    for user in users :
        if user['name'] == name and user['age'] == age :
            result.append(user) 
            
print(find_users_age('Alice', 25))