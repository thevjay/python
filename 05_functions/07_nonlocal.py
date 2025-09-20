def update_order():
    chai_type = "Masala Chai"  # Local scope
    def kitchen():
        nonlocal chai_type
        chai_type = "Ginger Chai"  # Modifying enclosing scope variable
        print(f"Kitchen: {chai_type}") 
    kitchen()
    print(f"Update Order: {chai_type}")
update_order()