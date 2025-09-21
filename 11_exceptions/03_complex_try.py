def serve_chai(flavor):
    try:
        print(f"Serving {flavor} chai.")
        if flavor == "unknown":
            raise ValueError("Unknown chai flavor!")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        print(f"{flavor} Chai served successfully.")
    finally:
        print("Thank you for visiting our chai shop!")

serve_chai("masala")
serve_chai("unknown")
# This code demonstrates handling exceptions using try and except blocks.
# It attempts to serve a chai flavor and raises a ValueError if the flavor is unknown.