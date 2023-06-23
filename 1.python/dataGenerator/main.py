import sys

from models import generateMultipleData

from models.user import User
from models.store import Store
from models.item import Item

from loadAndPrint import getUserInput, getCommandLineInput, printOps


if __name__=="__main__" :

    # ===============
    #   INPUT
    # ===============

    if (len(sys.argv) > 3) :
        type, num, output = getUserInput(sys.argv)

    else :
        type, num, output = getCommandLineInput()

    # ===============
    #   GENERATE
    # ===============

    selectModel = {
        "user" : User,
        "store" : Store,
        "item" : Item
    }
    data = generateMultipleData(selectModel[type], num)

    # ===============
    #   OUTPUT
    # ===============

    printOps(type, data, output)