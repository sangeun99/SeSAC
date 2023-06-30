

keyword="ko"
name="sdkfkojskdfjksdkosdfdfko"

for i in range(len(name)-len(keyword)+1) :
    print(name[i:i+len(keyword)], keyword)
    if name[i:i+len(keyword)] == keyword :
        print('!!!!')


data= []
match = [0 for _ in range(len(name))]
l = len(keyword)
for i in range(len(name)-l+1):
    if name[i:i+l] == keyword:
      data.append(i)
      match[i:i+l] = [1 for _ in range(i, i+l)]
print(data)
print(match)


match = [0 for _ in range(len(name))]
for i in range(len(name)-l+1):
    if name[i:i+len(keyword)] == keyword:
      match[i:i+len(keyword)] = [1 for _ in range(i, i+len(keyword))]
print(match)
# print([i for i in range(len(name)-len(keyword)+1) if name[i:i+len(keyword)] == keyword])

    
# name = user['Name']
# keyword = search_name
