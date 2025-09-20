# def make_chai():
#     # return "Ginger Chai"
#     print("This will never be printed")

# returned_chai = make_chai()
# print(returned_chai)

def idle_chaiwala():
    pass

print(idle_chaiwala())  # None

def sold_cups():
    return 5

total_cups = sold_cups() + 3
print(total_cups)

def chai_status(cups_left):
    if cups_left > 0:
        return "Chai is available"
    return "Chai is not available"
print(chai_status(3))
print(chai_status(0))

def chai_report():
    return 100,20,20 # sold , remaining
sold,remaining,not_paid = chai_report()
print(f"Sold: {sold}, Remaining: {remaining}")