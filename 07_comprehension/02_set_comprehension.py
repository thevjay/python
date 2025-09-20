favourite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Iced Tea",
    "Lemon Tea",
    "Green Tea",
    "Iced Green Tea",
]

unique_favourite_chais = {chai for chai in favourite_chais if len(chai) > 8}
print(unique_favourite_chais)

recipes = {
    "Masala Chai": ["Tea Leaves", "Water", "Milk", "Spices", "Sugar"],
    "Green Tea": ["Green Tea Leaves", "Water", "Lemon", "Honey"],
    "Iced Tea": ["Tea Leaves", "Water", "Ice", "Lemon", "Sugar"],
    "Lemon Tea": ["Tea Leaves", "Water", "Lemon", "Sugar"],
    "Iced Green Tea": ["Green Tea Leaves", "Water", "Ice", "Lemon", "Honey"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
