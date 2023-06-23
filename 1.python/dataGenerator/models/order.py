from generators.common.id import Id
from generators.order.storeid import StoreId
from generators.order.userid import UserId

class Order():
    
    def __init__(self):
        self.orderId = Id().generate()
        self.storeId = StoreId().generate()
        self.userId = UserId().generate()
    
    def generate(self) :
        generatedData = {
            "orderid" : self.orderId,
            "storeid" : self.storeId,
            "userid" : self.userId
        }
        return generatedData
