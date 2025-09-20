def pure_chai(cups):
    return cups * 10

total_chai = 0

# not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups * 10
    print(f"Total chai sold: {total_chai}")

def pour_chai(n):
    if n == 0:
        return "all done"
    print("Pouring chai...")
    return pour_chai(n-1) # recursion
print(pour_chai(5))

# lambda function
chai_types = ["Masala","Ginger","Elaichi","Ginger","Elaichi"]
strong_chai = list(filter(lambda chai: chai == "Ginger",chai_types))
print(strong_chai)
