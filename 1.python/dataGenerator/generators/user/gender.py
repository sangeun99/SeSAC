import random

from generators.generators import GeneratorBase

class Gender(GeneratorBase):
    def __init__(self):
        self.gender = random.choice(['Female', 'Male'])
    
    def generate(self) :
        return self.gender
