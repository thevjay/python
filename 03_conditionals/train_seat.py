seat_type = input("Enter seat tyepe (sleeper/AC/non-AC): ").lower()

match seat_type:
    case "sleeping":
        print("You chose sleeping seat")
    case "ac":
        print("You chose AC seat")
    case "non-ac":
        print("You chose non-AC seat")
    case _:
        print("Invalid seat type")