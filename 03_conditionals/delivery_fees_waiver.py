order_amount = int(input("Enter your order amount: "))

print(f"User entered {type(order_amount)}")

devlivery_fee = 0 if order_amount > 300 else 50

print(f"Delivery fee is {devlivery_fee}")