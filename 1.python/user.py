users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
]

def find_users(search_user) :
    result = []
    count = 0
    for user in users :
        for key in search_user.keys() :
            if user[key] != search_user[key] :
                break
            else :
                count += 1
                if count == len(search_user) :
                    result.append(user)
    return result
            
print(find_users({"name": "Bob", "age": 30}))
print(find_users({"name": "Bob"}))
print(find_users({"name": "Bob", "location": "Busan", "car": "Mercedes"}))
print(find_users({"location": "Busan", "car": "Mercedes"}))