import uuid

from generators.generators import GeneratorBase

class Id(GeneratorBase):
    def __init__(self):
        self.id = uuid.uuid4()
    
    def generate(self):
        return self.id
    