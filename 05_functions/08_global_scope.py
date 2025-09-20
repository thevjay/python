chai_type = "Plain"

def front_desk():

    def kitchen():
        global chai_type
        chai_type = "Masala Chai"
        print(f"Kitchen: {chai_type}")
    kitchen()
    print(f"Front Desk: {chai_type}")

front_desk()
print(f"Global: {chai_type}")
