# Task 3.10 - Car Parking Simulator
# Simulate a parking facility with entry/exit, capacity limit,
# and occupancy checking.


class Parking:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self._capacity = capacity
        self._spots: dict[str, str] = {}   # plate -> spot_number

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def occupied(self) -> int:
        return len(self._spots)

    @property
    def available(self) -> int:
        return self._capacity - self.occupied

    def enter(self, plate: str) -> str:
        plate = plate.strip().upper()
        if not plate:
            return "Error: license plate cannot be empty"
        if plate in self._spots:
            return f"Error: vehicle '{plate}' is already parked (spot {self._spots[plate]})"
        if self.available == 0:
            return f"Error: parking is full ({self._capacity}/{self._capacity} spots taken)"

        spot = f"A{self.occupied + 1:02d}"
        self._spots[plate] = spot
        return f"Vehicle '{plate}' parked at spot {spot}. Occupancy: {self.occupied}/{self._capacity}"

    def exit(self, plate: str) -> str:
        plate = plate.strip().upper()
        if plate not in self._spots:
            return f"Error: vehicle '{plate}' is not currently parked here"
        spot = self._spots.pop(plate)
        return f"Vehicle '{plate}' left spot {spot}. Occupancy: {self.occupied}/{self._capacity}"

    def status(self) -> str:
        lines = [f"=== Parking Status: {self.occupied}/{self._capacity} spots occupied ==="]
        if self._spots:
            for plate, spot in self._spots.items():
                lines.append(f"  Spot {spot}: {plate}")
        else:
            lines.append("  (empty)")
        return "\n".join(lines)


# --- Demo ---
if __name__ == "__main__":
    parking = Parking(capacity=4)
    print(parking.status())
    print()

    events = [
        ("enter", "AA1234BB"),
        ("enter", "BC5678CD"),
        ("enter", "EF9012GH"),
        ("enter", "IJ3456KL"),
        ("enter", "MN7890OP"),   # parking full
        ("enter", "AA1234BB"),   # already inside
        ("exit",  "BC5678CD"),
        ("enter", "MN7890OP"),   # now there's room
        ("exit",  "ZZ0000ZZ"),   # not in parking
    ]

    for action, plate in events:
        if action == "enter":
            print(parking.enter(plate))
        elif action == "exit":
            print(parking.exit(plate))

    print()
    print(parking.status())
