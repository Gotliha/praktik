# Task 2.1 - Linear Search: Product Finder
# Find a product in an online store array.
# Returns position (indexed from 1) or -1 if not found.


def find_product(products: list, target: str) -> int:
    for i in range(len(products)):
        if products[i] == target:
            return i + 1
    return -1


# --- Demo ---
if __name__ == "__main__":
    store = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Webcam", "USB Hub"]

    queries = ["Mouse", "Webcam", "Tablet"]
    for query in queries:
        result = find_product(store, query)
        if result != -1:
            print(f"'{query}' found at position {result}")
        else:
            print(f"'{query}' — Product not found")
