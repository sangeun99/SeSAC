from generators.common.address import Address
from generators.user.name import Name
from generators.store.storename import StoreName

def loadFiles(filename, target):
    try :
        f = open(filename, 'r', encoding='UTF8')
        for line in f.readlines() :
            target.append(line.strip())  
        f.close
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

loadFiles('src/firstname.txt', Name.firstnames)
loadFiles('src/lastname.txt', Name.lastnames)
loadFiles('src/cities.txt', Address.cities)
loadFiles('src/gus.txt', Address.gus)
loadFiles('src/storetypes.txt', StoreName.types)
loadFiles('src/storelocations.txt', StoreName.storelocations)
print("Loaded 6 files")