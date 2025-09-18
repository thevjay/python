chai_order = dict(type="chai",quantity=2,price=4.99)
print(chai_order)

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "water"
chai_recipe["spices"] = ["ginger","cardamom","cinnamon"]

# print(f"Chai recipe: {chai_recipe["base"]} with {chai_recipe["liquid"]} ")

chai_order = {"type":"chai","quantity":2,"price":4.99}

print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}") 
print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed item: {last_item}")

extra_spices = {"cloves","black ","pepper"}
chai_recipe.update(extra_spices)
print(f"Chai recipe: {chai_recipe}")

chai_size = chai_order.get("size","medium")
print(f"Chai size: {chai_size}")