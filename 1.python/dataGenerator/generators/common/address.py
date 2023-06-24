import random

from generators.generators import GeneratorBase

class Address(GeneratorBase):
    cities = []
    gus = []
    streetforms = ['길', '로']

    ADDRESSMAX = 99

    def __init__(self) :
        city = random.choice(Address.cities)
        gu = random.choice(Address.gus)
        street1 = random.randint(1, Address.ADDRESSMAX)
        streetform = random.choice(Address.streetforms)
        street2 = random.randint(1, Address.ADDRESSMAX)
        self.address = f'{city} {gu} {street1}{streetform} {street2}'

    def generate(self):
        return self.address