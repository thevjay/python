is_boiling = True
stri_count = 5
total_actions =stri_count + is_boiling # upcasting
print(f"Total actions: {total_actions}")

# result = 6

milk_present = True
print(f"Milk present: {bool(milk_present)}")

water_hot = True
tea_added = False

can_serve_tea = water_hot and tea_added
print(f"Can serve tea: {can_serve_tea}")