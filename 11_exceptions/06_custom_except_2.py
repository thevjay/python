class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Not enough ingredients to make chai...")
    print("Chai is ready!")

make_chai(0, 1)  # This will raise OutOfIngredientsError
# This code demonstrates how to create and raise a custom exception in Python.
