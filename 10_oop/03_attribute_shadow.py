class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)  # hot
print(cutting.strength)     # strong

cutting.temperature = "cold"
print(cutting.temperature)  # cold

del cutting.temperature
print(cutting.temperature)  # hot