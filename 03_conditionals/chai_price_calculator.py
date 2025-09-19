cup = input("Choose your cup size (small/medium/large): ").lower()

print(f"You selected a {cup} cup.")

if cup == "small":
    price = 2.50
elif cup == "medium":
    price = 3.00
elif cup == "large":
    price = 3.50
else:
    price = 0
    print("Invalid cup size selected.")