numbers = [1,2,3,4,5,6,2,4,6,2,1]

def remove_duplicate(numlist) :
    unique_list = []
    for n in numbers :
        if not n in unique_list :
            unique_list.append(n)
    return unique_list

print("원본리스트:", numbers)
print("유닉리스트:", remove_duplicate(numbers))