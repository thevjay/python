ingredients = ["water", "milk","black tea"]

ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")

ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger","cardamom"]
chai_ingredients = ["water","milk"]

chai_ingredients.extend(spice_options)
print(f"Ingredients are: {chai_ingredients}")

chai_ingredients.insert(2,"black tea")
print(f"Ingredients are: {chai_ingredients}")

last_ingredient = chai_ingredients.pop()
print(f"Removed ingredient: {last_ingredient}")

chai_ingredients.reverse()
print(f"Ingredients are: {chai_ingredients}")

chai_ingredients.sort()
print(f"Ingredients are: {chai_ingredients}")

# min
# max

# 2 + 3
# operatorOverloading
base_liquid = ["water","milk"]
extra_flavor = ["ginger"]

full_liquid = base_liquid + extra_flavor
print(full_liquid)

strong_tea = ["black tea"] * 3
print(strong_tea)