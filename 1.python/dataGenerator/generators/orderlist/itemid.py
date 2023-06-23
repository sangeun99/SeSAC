import random

from generators.generators import GeneratorBase

class ItemId(GeneratorBase):
    
    items = []

    def __init__(self):
        itemInfo = random.choice(ItemId.items)
        self.itemId = itemInfo[0]
        
    def generate(self):
        return self.itemId