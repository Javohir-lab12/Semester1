items = ["Apple", "Banana", "Cherry"]
prices = [0.50, 0.30, 0.10]
quantities = [4, 2, 10]
grand_total = 0
for i, (item, price, quantity) in enumerate(zip(items, prices, quantities),1):
    total = price * quantity
    print(f'Line #{i}: {item} x{quantity} = ${total}')
    grand_total += total
print("--------------------")
print(f"Grand total: ${grand_total}")
