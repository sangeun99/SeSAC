from abc import *

class GeneratorBase(metaclass=ABCMeta):
    @abstractmethod
    def generate(self):
        pass    