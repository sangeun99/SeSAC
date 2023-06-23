from generators.common.address import Address
from generators.common.id import Id
from generators.user.name import Name
from generators.user.birthdate import Birthdate
from generators.user.gender import Gender

class User:
    def __init__(self) :
        self.id = Id().generate()
        self.name = Name().generate()
        self.gender = Gender().generate()
        newBirthdate = Birthdate()
        self.age = newBirthdate.generateAge()
        self.birthdate = newBirthdate.generate()
        self.address = Address().generate()

    def generate(self):
        generatedData = {
            "id" : self.id, 
            "name" : self.name, 
            "gender" : self.gender, 
            'age' : self.age, 
            "birthdate" : self.birthdate, 
            'address' : self.address
        }
        return generatedData
