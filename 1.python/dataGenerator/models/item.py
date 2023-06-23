from generators.common.id import Id
from generators.item.singleitem import SingleItem

class Item:
    def __init__(self) :
        self.itemId = Id().generate()
        newItem = SingleItem()
        self.itemName = newItem.generate()
        self.itemType = newItem.generateType()
        self.unitPrice = newItem.generateUnitPrice()

    def generate(self) :
        generatedData = {
            "id" : self.itemId,
            "name" : self.itemName,
            "type" : self.itemType,
            "price" : self.unitPrice
        }
        return generatedData
