def add_vat(price, vat_rate):
    return price + (100 * vat_rate / 100)


orders = [100, 200, 300]

for order in orders:
    final_price = add_vat(order, 5)
    print(final_price)
