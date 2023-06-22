import random

class Gender():
    def __init__(self):
        self.gender = random.choice(['Female', 'Male'])
    
    def generate(self) :
        return self.gender
