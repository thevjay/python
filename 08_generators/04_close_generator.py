def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha Chai"
    yield "Turmeric Chai"
    
def full_menu():
    yield from local_chai()
    yield from imported_chai()
    yield "Cardamom Chai"

# Example usage:
for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for your order..."
    except:
        print("Closing the stall. Thank you for visiting!")

stall = chai_stall()
next(next(stall))
stall.close()  # Start the generator
print(stall.send("masala"))  # Place an order for masala chain