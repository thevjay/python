menu = [
    "masala chai",
    "ginger chai",
    "cardamom chai",
    "tulsi chai",
    "regular chai",
]

# iced_tea = [my_tea for my_tea in menu if "tulsi" in my_tea]

iced_tea = [my_tea for my_tea in menu if len(my_tea) > 10]

print(iced_tea)  