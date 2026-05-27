# Task 2.6 - Merge Sorted Orders
# Merge two sorted-by-time order lists in chronological order.
# Complexity: O(n + m). No built-in sort allowed.
# Each order: (timestamp_str, order_id, description)


def merge_orders(web_orders: list, app_orders: list) -> list:
    merged = []
    i, j = 0, 0

    while i < len(web_orders) and j < len(app_orders):
        if web_orders[i][0] <= app_orders[j][0]:
            merged.append(web_orders[i])
            i += 1
        else:
            merged.append(app_orders[j])
            j += 1

    while i < len(web_orders):
        merged.append(web_orders[i])
        i += 1

    while j < len(app_orders):
        merged.append(app_orders[j])
        j += 1

    return merged


# --- Demo ---
if __name__ == "__main__":
    web_orders = [
        ("2024-01-01 08:15", "W001", "Laptop"),
        ("2024-01-01 10:30", "W002", "Mouse"),
        ("2024-01-01 14:00", "W003", "Monitor"),
    ]

    app_orders = [
        ("2024-01-01 09:00", "A001", "Keyboard"),
        ("2024-01-01 11:45", "A002", "Headphones"),
        ("2024-01-01 16:20", "A003", "Webcam"),
    ]

    result = merge_orders(web_orders, app_orders)

    print(f"{'Time':<22} {'ID':<8} {'Item'}")
    print("-" * 45)
    for time, order_id, item in result:
        print(f"{time:<22} {order_id:<8} {item}")
