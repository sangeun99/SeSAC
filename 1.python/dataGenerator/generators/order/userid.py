import random

from generators.generators import GeneratorBase

class UserId(GeneratorBase) :
    
    users = []
    # scr : results/store.csv
    
    def __init__(self): 
        userInfo = random.choice(UserId.users)
        self.userId = userInfo[0]

    def generate(self):
        return self.userId