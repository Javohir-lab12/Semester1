def group_packages(shipment_list):
    shipping_dict = {}
    for c in shipment_list:
        city, packageid, weightkg = c.split("|")
        weightkg = int(weightkg)
        if city not in shipping_dict:
            shipping_dict[city] = []
        shipping_dict[city].append((packageid , weightkg))
    return shipping_dict

def calculate_truck_loads(shipping_dict):
    for city , list in shipping_dict.items():
        total = 0
        for c in list:
            total += c[1]
        print(f"{city}: {total} kg total")

shipment_list = [
    "New York|Box101|50",
    "Chicago|Box102|20",
    "New York|Box103|30",
    "Miami|Box104|15",
    "Chicago|Box105|45",
    "New York|Box106|10"
]
shipping_dict = group_packages(shipment_list)
calculate_truck_loads(shipping_dict)