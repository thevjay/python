class chaiOrder:
    def __init__(self,type_,size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml {self.type} chai"

order_one = chaiOrder("Masala",150)
print(order_one.summary())

order_two = chaiOrder("Ginger",100)
print(order_two.summary())