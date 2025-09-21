chai_menu = {"masala": 50, "ginger": 60, "cardamom": 70}

# chai_menu["saffron"]  # This will raise a KeyError

try:
    chai_menu["saffron"] # This will raise a KeyError
except KeyError:
    print("The specified key does not exist in the dictionary.")
