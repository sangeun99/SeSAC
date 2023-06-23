import random

from generators.generators import GeneratorBase

class OrderId(GeneratorBase):
    
    orders = []

    def __init__(self):
        orderInfo = random.choice(OrderId.orders)
        self.orderId = orderInfo[0]
        
    def generate(self):
        return self.orderId