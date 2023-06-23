import random

from generators.generators import GeneratorBase

class StoreId(GeneratorBase) :
    
    stores = []
    # scr : results/store.csv
    
    def __init__(self): 
        storeInfo = random.choice(StoreId.stores)
        self.storeId = storeInfo[0]

    def generate(self):
        return self.storeId