print("SHOPPING CART CALCULATOR")
print("="*40)
def calculate_item_total(quantity, unit_price):
     total = quantity * unit_price
     return total
def apply_bulk_discount(total, quantity):
    if quantity >= 10:
        return total * 0.10
    elif quantity >= 5:
        return total * 0.05
    else:
        return 0
def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate/100

def is_eligible_for_free_shipping(subtotal):
    return subtotal >= 50    
def process_order(item_name, quantity, unit_price, tax_rate):
    item_total = calculate_item_total(quantity,unit_price)
    discount = apply_bulk_discount(item_total, quantity)
    subtotal = item_total - discount
    final_total = subtotal + calculate_tax(subtotal, tax_rate)
    print(f"Order Receipt for: {item_name}")
    print(f"  Quantity: ${quantity} @ ${unit_price} for each")
    print(f"  Item Total: {calculate_item_total(quantity, unit_price)}")
    print(f"  Bulk Discount: {discount}")
    print(f"  Subtotal: {subtotal}")
    print(f"  Tax {tax_rate}%: {calculate_tax(subtotal, tax_rate)}")
    print(f"  Final Total: ${subtotal + calculate_tax(subtotal, tax_rate)}")
    if subtotal < 50:
        print(f"Need ${50 - final_total} more for free shipping")
print(process_order("Notebook", 5, 3, 8))
print("-"*40)
