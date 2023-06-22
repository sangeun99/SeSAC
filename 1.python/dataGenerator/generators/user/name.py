import random

class Name:
    
    firstnames = []
    lastnames = []

    def __init__(self) :
        self.name = random.choice(Name.lastnames) \
                  + random.choice(Name.firstnames)
    
    def generate(self) :
        return self.name