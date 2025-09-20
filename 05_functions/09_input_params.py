# chai = "Ginger chai"

# def prepare_chai(order):
#     print(f"Preparing {order}")

# prepare_chai(chai)
# prepare_chai("Adrak Chai")

chai = [1,2,3]

# def edit_chai(cup):
#   print(f"Editing {cup}")

def make_chai(tea,milk,sugar,tea_leaves):
    print(f"Making chai with {tea} tea, {milk} cup of milk, {sugar} spoons of sugar and {tea_leaves} spoons of tea leaves")

make_chai("Ginger",1,2,3)  # positional arguments
make_chai(tea="Ginger",milk=1,sugar=2,tea_leaves=3)  # keyword arguments


def special_chai(*args,**kwargs): # variable length arguments
    print("Ingredients:",args) #
    print("Extras:",kwargs) #

special_chai("Ginger","Elaichi",sugar=2,tea_leaves=3) #
special_chai("Adrak","Elaichi",milk=1,sugar=2,tea_leaves=3)

def order_chai(size,*args,**kwargs): # variable length arguments
    print(f"Order size: {size}")
    print("Ingredients:",args) #
    print("Extras:",kwargs) #
order_chai("Large","Ginger","Elaichi",sugar=2,tea_leaves=3) #


# def chai_order(order=[]):
#     order.append("Ginger Chai")
# #     print(order)
# chai_order()  # ["Ginger Chai"]
# chai_order()  # ["Ginger Chai","Ginger Chai"]


def chai_order(order=None):
    if order is None:
        order = []
    order.append("Ginger Chai")
    print(order)

chai_order() 
chai_order() 