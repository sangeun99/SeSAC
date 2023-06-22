from generators.common.address import Address
from generators.user.name import Name
from generators.user.birthdate import Birthdate
from generators.user.gender import Gender

class User:
    def __init__(self) :
        self.name = Name().generate()
        self.gender = Gender().generate()
        newBirthdate = Birthdate()
        self.age = newBirthdate.generateAge()
        self.birthdate = newBirthdate.generate()
        self.address = Address().generate()

    def generate(self):
        return self.name, self.gender, self.age, self.birthdate, self.address
