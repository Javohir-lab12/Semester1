def rent_vehicle(drivers_db, fleet_catalog, driver_id, model, days):
    if driver_id not in drivers_db:
        raise KeyError("Driver not found")
    if model not in fleet_catalog:
        raise KeyError ("Vehicle model unavailable")
    if not isinstance(days , int) or days<1:
        raise ValueError ("Days must be positive integer")
    total = days * fleet_catalog[model]["rate"]
    if drivers_db[driver_id]["age"] < 25:
        total += fleet_catalog[model]["surcharge"]
    if drivers_db[driver_id]["credit"] < total:
        raise ValueError("Credit limit exceeded")
    drivers_db[driver_id]["credit"] = drivers_db[driver_id]["credit"] - total
    return float(total)


def process_rentals(drivers_db, fleet_catalog, rental_list):
    total_profit = 0
    rejected_requests = 0
    for driver_id , model , days in rental_list:
        try:
            cost = rent_vehicle(drivers_db, fleet_catalog, driver_id, model, days)
            total_profit += cost
        except (KeyError, ValueError) as e:
            print(f"Rental Error for {driver_id}: {e}")
            rejected_requests += 1
    return {'total_profit': float(total_profit), 'rejected_requests': int(rejected_requests)}

# Format: {Model: {"rate": float, "surcharge": float}}
fleet = {
    "Sedan": {"rate": 50.0, "surcharge": 25.0},
    "SUV":   {"rate": 80.0, "surcharge": 40.0}
}

# Format: {DriverID: {"credit": float, "age": int}}
drivers = {
    "D1": {"credit": 200.0, "age": 30}, # No surcharge
    "D2": {"credit": 100.0, "age": 20}  # Pays surcharge
}

rentals = [
    ("D1", "Sedan", 3),    # Valid. Cost: 150. Rem: 50.
    ("D2", "Sedan", 2),    # Error: Cost (50*2)+25 = 125 > 100.
    ("D1", "Truck", 1),    # Error: Vehicle model unavailable.
    ("D1", "Sedan", -1),   # Error: Days must be positive.
    ("D9", "SUV", 1)       # Error: Driver not found.
]
print(process_rentals(drivers, fleet, rentals))