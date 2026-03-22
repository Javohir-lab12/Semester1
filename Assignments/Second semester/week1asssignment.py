class ParkingSpot:
    lot_name = "City Center Parking"
    max_vehicles = 3
    total_spots = 0
    def __init__(self, spot_number, level):
        self.spot_number = spot_number
        self.level = level
        self.vehicles = []
        ParkingSpot.total_spots += 1
    def park_vehicle(self, plate):
        if len(self.vehicles) == ParkingSpot.max_vehicles:
            print("Spot is full")
        else:
            self.vehicles.append(plate)
            print(f"Parked vehicle {plate} at Spot {self.spot_number}")
    def remove_vehicle(self, plate):
        if plate in self.vehicles:
            self.vehicles.remove(plate)
            print(f"Removed vehicle {plate} from Spot {self.spot_number}")
        else:
            print("Vehicle not found")
    def display_spot(self):
        print(f"Spot {self.spot_number} on Level {self.level} at {self.lot_name}")

Spot1 = ParkingSpot(42, "B2")
Spot1.display_spot()
Spot1.park_vehicle("AA 123")
Spot1.park_vehicle("BB 456")
Spot1.park_vehicle("CC 789")
Spot1.park_vehicle("DD 000")
Spot1.remove_vehicle("BB 456")
Spot1.remove_vehicle("ZZ 999")
print(f"Total spots: {ParkingSpot.total_spots}")