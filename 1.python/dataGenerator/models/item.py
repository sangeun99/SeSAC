from generators.item.singleitem import SingleItem

class Item:

    header = ('name', 'type', 'price') 

    def __init__(self) :
        newItem = SingleItem()
        self.itemName = newItem.generate()
        self.itemType = newItem.generateType()
        self.unitPrice = newItem.generateUnitPrice()

    def generate(self) :
        return self.itemName, self.itemType, self.unitPrice
