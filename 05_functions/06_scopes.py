def serve_chai():
    chai_type = "Masala Chai" # Local scope
    print(f"Serving {chai_type}")

chai_type = "Adrak Chai"
serve_chai()
print(f"Chai type outside function: {chai_type}")

def chai_counter():
    chai_order = "lemon chai" # Enclosing scope
    def print_order():
        chai_type = "Ginger Chai" # Local scope
        print(f"Inner: {chai_order}")
    print_order()
    print(f"Outer {chai_type}")
chai_order = "Tulsi" # Global scope
chai_counter()
print("Global:", chai_order)