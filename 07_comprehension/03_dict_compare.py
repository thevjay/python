tea_prices_inr = {
    "iced matcha latte": 250,
    "iced hojicha latte": 250,
    "iced chocolate": 200,
    "hot matcha latte": 200,
    "hot hojicha latte": 200,
}    

tea_prices_usd = { tea:price / 80 for tea,price in tea_prices_inr.items() if "iced" in tea }
print(tea_prices_usd)