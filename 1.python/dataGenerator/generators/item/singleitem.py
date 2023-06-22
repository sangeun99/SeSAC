import random

from generators.generators import GeneratorBase

class SingleItem(GeneratorBase):
    itemTypes = {
             "Coffee": {
                "Americano": 3000,
                "Latte": 4000,
                "Espresso": 2500,
                "Cappuccino": 4500,
                "Mocha": 5000
            },
            "Juice": {
                "Orange": 2000,
                "Apple": 2500,
                "Grape": 3000,
                "Pineapple": 3500,
                "Watermelon": 4000
            },
            "Cake": {
                "Chocolate": 6000,
                "Strawberry": 5500,
                "Vanilla": 5000,
                "Red Velvet": 6500,
                "Carrot": 6000
            }
        }
    
    def __init__(self):
        typeIndex = random.randrange(len(SingleItem.itemTypes))
        self.itemType = list(SingleItem.itemTypes.keys())[typeIndex]
        itemList = list(SingleItem.itemTypes.values())[typeIndex]
        itemIndex = random.randrange(len(itemList))
        self.itemName = list(itemList.keys())[itemIndex]
        self.unitPrice = list(itemList.values())[itemIndex]

    def generate(self):
        return self.itemName
    
    def generateType(self):
        return self.itemType
    
    def generateUnitPrice(self):
        return self.unitPrice