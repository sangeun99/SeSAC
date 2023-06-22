import random
 
class StoreName:
    
    types = []
    storelocations = []

    def __init__(self) :
        self.type = random.choice(StoreName.types)
        location = random.choice(StoreName.storelocations)
        self.name = f'{self.type} {location}{random.randint(1,10)}호점'
    
    def generate(self) :
        return self.name
    
    def generateType(self) :
        return self.type