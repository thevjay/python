def process_order(item, quantity):
    try:
        price = {"apple": 100, "banana": 50, "orange": 70}[item]
        total_cost = price * quantity
        print(f"Total cost for {quantity} {item}(s): {total_cost}")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative!")
    except KeyError:
        print(f"Error: {item} is not available in the menu.")
    except ValueError as ve:
        print(f"Error: {ve}")

process_order("apple", 3)
process_order("grape", 2)
process_order("banana", -1)