def add_product(products, prices, new_product, new_price):
    products.append(new_product)
    prices.append(new_price)

def remove_product(products, prices, product_to_remove):
    for index in range(len(products)):
        if product_to_remove == products[index]:
            products.pop(index)
            prices.pop(index)
            return True
    return False
    
def get_most_valuable(products, prices, count):
    new_list_in_order = []
    temp_products = products[:]
    temp_prices = prices[:]
    for i in range(count):
        highest_index = 0
        for j in range (len(temp_prices)):    
            if temp_prices[j] > temp_prices[highest_index]:
                highest_index = j
        new_list_in_order.append(temp_products[highest_index]) 
        temp_products.pop(highest_index)
        temp_prices.pop(highest_index)

    return new_list_in_order

def manage_inventory(initial_products, initial_prices, new_product_data, product_to_remove, top_count):
    products_copy = initial_products[:]
    prices_copy = initial_prices[:]
    new_product, new_price = new_product_data[0], new_product_data[1]
    add_product(products_copy, prices_copy, new_product, new_price)
    remove_product(products_copy, prices_copy, product_to_remove)
    final_products_list = products_copy
    top_product_names = get_most_valuable(products_copy, prices_copy, top_count)
    return final_products_list, top_product_names

# Test Case 1
products = ["Watch", "Ring", "Bag", "Scarf", "Pen"]
prices = [5500.00, 7200.00, 3100.00, 800.00, 1200.00]
new_product = ["Statue", 6800.00]
remove_name = "Scarf"
count = 3

# When you call your function:
final_products, top_list = manage_inventory(products, prices, new_product, remove_name, count)
print("Final products:", final_products)
print("Top list:", top_list)