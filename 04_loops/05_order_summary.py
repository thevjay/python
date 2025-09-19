names = ["John", "Jane", "Doe"]
bills = [23.45, 67.89, 12.34]

for name,amount in zip(names, bills):
    print(f"{name}: ${amount:.2f}")