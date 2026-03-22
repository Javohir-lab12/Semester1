print("=== Food Truck Order System ===")
print("Enter food type: appetizer, entree, or dessert")
print("Type 'done' when finished ordering")
print()
appetizer = 5.00 
entree = 11.00
dessert = 6.50 
total = 0
while True:
    user_input = input("Enter food type: ")
    if user_input == "done":
        print("=== Order Summary ===")
        print(f"Subtotal: ${total}")
        if total >= 35:
            print("Combo Deal Discount: -$4.50")
            print(f"Final Total: ${total - 4.5}")
        else:
            print(f"Final Total: ${total}")
        print("Thank you for your order!")
        break
    elif user_input == "appetizer":
        print(f"Price: ${appetizer}")
        total = total + appetizer
        print(f"Current total: ${total}\n")
    elif user_input == "entree":
        print(f"Price: ${entree}")
        total = total + entree
        print(f"Current total: ${total}\n")
    elif user_input == "dessert":
        print(f"Price: ${dessert}")
        total = total + dessert
        print(f"Current total: #{total}\n")
    else:
        print("Invalid input. Please enter apetizer, entree, dessert or done\n")
