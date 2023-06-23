from generators.common.id import Id
from generators.orderlist.orderid import OrderId
from generators.orderlist.itemid import ItemId

class Orderlist():
    # Id,OrderId,ItemId
    def __init__(self):
        self.id = Id().generate()
        self.orderId = OrderId().generate()
        self.itemId = ItemId().generate()

    def generate(self):
        generatedData = {
            "id" : self.id,
            "orderid" : self.orderId,
            "itemid" : self.itemId
        }
        return generatedData