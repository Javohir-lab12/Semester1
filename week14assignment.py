def map_orders(order_log):
    order_dict = {}
    for order in order_log:
        order_dict[order["tracking_num"]] = order["customer_city"]
    return order_dict

def check_shipments(order_map, scanned_tracking_nums):
    order_set = set(order_map)
    scanned_tracking = set(scanned_tracking_nums)
    delayed_orders = order_set - scanned_tracking
    phantom_shipments = scanned_tracking - order_set
    return delayed_orders, phantom_shipments

def format_delay_notices(order_map, delayed_set):
    formatted_list = [f"DELAYED: Package {tracking} to {order_map[tracking]}" for tracking in delayed_set]
    formatted_list.sort(key = lambda x : x.split(" to ")[1])
    return formatted_list

orders = [
    {'tracking_num': "TN100", 'customer_city': "New York"},
    {'tracking_num': "TN101", 'customer_city': "London"},
    {'tracking_num': "TN102", 'customer_city': "Tokyo"}
]

scanned = ["TN100", "TN102", "TN999"]
order_map = map_orders(orders)
delayed, phantom = check_shipments(order_map, scanned)
report = format_delay_notices(order_map, delayed)
print(f"Delayed Orders: {delayed}")
print(f"Phantom Shipments: {phantom}")
print(f"Report: {report}")