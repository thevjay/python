class InvalidChaiError(Exception):
    pass

def bill(flavor,cups):
    menu = {"masala": 50, "ginger": 60, "cardamom": 70}
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"{flavor} is not available in the menu...")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be a positive integer.")
        total_cost = menu[flavor] * cups
        print(f"Total cost for {cups} cup(s) of {flavor} chai: {total_cost}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thank you for visiting our chai shop!")

bill("masala", 3)
bill("saffron", 2)
bill("ginger", -1)
bill("cardamom", "two")

