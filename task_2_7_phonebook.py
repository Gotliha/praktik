# Task 2.7 - Hash Table: PhoneBook
# Phone book with custom hash table.
# Custom hash function, chaining for collisions,
# auto-resize when load factor > 0.75. No built-in dict allowed.


class PhoneBook:
    def __init__(self, initial_capacity: int = 8):
        self._capacity = initial_capacity
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]

    # --- Hash function ---
    def _hash(self, key: str) -> int:
        h = 0
        for ch in key:
            h = (h * 31 + ord(ch)) % self._capacity
        return h

    # --- Resize when load factor > 0.75 ---
    def _resize(self):
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for bucket in old_buckets:
            for name, phone in bucket:
                self.add(name, phone)

    # --- Add or update contact ---
    def add(self, name: str, phone: str) -> None:
        if self._size / self._capacity > 0.75:
            self._resize()
        idx = self._hash(name)
        for i, (k, _) in enumerate(self._buckets[idx]):
            if k == name:
                self._buckets[idx][i] = (name, phone)
                return
        self._buckets[idx].append((name, phone))
        self._size += 1

    # --- Get phone by name ---
    def get(self, name: str) -> str | None:
        idx = self._hash(name)
        for k, v in self._buckets[idx]:
            if k == name:
                return v
        return None

    # --- Delete contact ---
    def delete(self, name: str) -> bool:
        idx = self._hash(name)
        for i, (k, _) in enumerate(self._buckets[idx]):
            if k == name:
                self._buckets[idx].pop(i)
                self._size -= 1
                return True
        return False

    # --- Check if contact exists ---
    def contains(self, name: str) -> bool:
        return self.get(name) is not None

    # --- Number of contacts ---
    def count(self) -> int:
        return self._size


# --- Demo ---
if __name__ == "__main__":
    pb = PhoneBook()

    contacts = [
        ("Alice",   "+1-555-0101"),
        ("Bob",     "+1-555-0202"),
        ("Charlie", "+1-555-0303"),
        ("Diana",   "+1-555-0404"),
        ("Eve",     "+1-555-0505"),
    ]

    for name, phone in contacts:
        pb.add(name, phone)

    print(f"Total contacts: {pb.count()}")
    print(f"Alice's phone:  {pb.get('Alice')}")
    print(f"Contains 'Bob': {pb.contains('Bob')}")

    pb.add("Alice", "+1-555-9999")  # update
    print(f"Alice updated:  {pb.get('Alice')}")

    pb.delete("Bob")
    print(f"After deleting Bob, total: {pb.count()}")
    print(f"Bob's phone: {pb.get('Bob')}")
