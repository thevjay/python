def chai_customer():
    print("Welcome to the chai shop!")
    order = yield
    while True:
        print(f"Preparing your {order} chai...")
        order = yield f"Here is your {order} chai! Enjoy!"
        print("What would you like next?")

# Example usage:
stall = chai_customer()
next(stall)  # Start the generator
print(stall.send("masala"))  # Place an order for masala chai
print(stall.send("ginger"))  # Place an order for ginger chai