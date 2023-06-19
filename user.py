users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
]


search_user = {"name": "Bob", "age": 30}

def find_users(search_user) :
    result = []
    for user in users :
        for key in search_user.keys() :
            if user[key] != search_user[key] :
                break
            result.append(user)
    return result
            
print(find_users(search_user))
