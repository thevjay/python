def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "cardamom"]:
        raise ValueError(f"{flavor} is not a valid chai flavor......")
    print(f"Brewed a cup of {flavor} chai.")

brew_chai("mas")
