from generators.common.address import Address
from generators.common.id import Id
from generators.store.storename import StoreName

class Store:
    def __init__(self) :
        self.id = Id().generate()
        newStoreName = StoreName()
        self.name = newStoreName.generate()
        self.type = newStoreName.generateType()
        self.address = Address().generate()

    def generate(self):
        generatedData = {
            "id" : self.id, 
            "name" : self.name, 
            "type" : self.type, 
            "address" : self.address
        }
        return generatedData