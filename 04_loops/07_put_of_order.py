flavours = ["Ginger", "Chocolate", "Vanilla", "Strawberry"]

for flavour in flavours:
    if flavour == "Chocolate":
        continue
    if flavour == "Vanilla":
        break
    print(f"{flavour} is not available.")
print("Enjoy your ice cream!")