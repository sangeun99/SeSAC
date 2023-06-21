with open("names.txt", "r") as file : # r = read, w = write, a = append
    names = file.read()
    print(names)


with open("names.txt", "r") as file : 
    lines = file.readlines()

names = []
for line in lines:
    names.append(line.strip())