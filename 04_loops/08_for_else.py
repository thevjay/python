staff = [("John", "Manager"), ("Doe", "Chef"), ("Jane", "Waiter")]

for name,age in staff:
    if name == "Doe":
        print("Found the chef!")
        break
else:
    print("Chef not found.")