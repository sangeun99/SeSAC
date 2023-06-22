from generators.common.address import Address
from generators.store.storename import StoreName

class Store:
    def __init__(self) :
        newStoreName = StoreName()
        self.name = newStoreName.generate()
        self.type = newStoreName.generateType()
        self.address = Address().generate()

    def generate(self):
        return self.name, self.type, self.address