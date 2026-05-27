# Task 3.2 - Order Processing Algorithm
#
# ─── VERBAL DESCRIPTION ──────────────────────────────────────────
# Input:  customer_id (str), items (list of dicts with name/qty/price),
#         payment_method (str), discount (float 0.0–1.0)
# Output: receipt (dict) or error message (str)
# Constraints: items list must not be empty; stock must be sufficient;
#              total must be > 0; payment method must be valid.
#
# Steps:
#   1. Validate customer_id and items list (not empty).
#   2. Check stock availability for each item.
#   3. Calculate subtotal (qty * price for each item).
#   4. Apply discount to subtotal.
#   5. Validate payment method.
#   6. Process payment (simulate success/failure).
#   7. Deduct items from stock.
#   8. Generate and return receipt.
#
# ─── FLOWCHART (ASCII) ───────────────────────────────────────────
#
#        [START]
#           │
#     [Validate input]
#      ┌────┴────┐
#    Invalid   Valid
#      │          │
#  [Return     [Check stock]
#   error]    ┌────┴────┐
#           Out of     In stock
#           stock         │
#             │      [Calc subtotal]
#         [Return          │
#          error]    [Apply discount]
#                          │
#                   [Validate payment]
#                    ┌─────┴─────┐
#                  Invalid     Valid
#                    │           │
#                [Return    [Process payment]
#                 error]    ┌────┴────┐
#                         Failed   Success
#                           │         │
#                       [Return  [Update stock]
#                        error]       │
#                               [Generate receipt]
#                                     │
#                                  [END]
# ─────────────────────────────────────────────────────────────────

VALID_PAYMENT_METHODS = {"card", "cash", "paypal"}

# Simulated stock
STOCK = {
    "Laptop":   10,
    "Mouse":    50,
    "Keyboard": 30,
    "Monitor":   5,
}


def process_order(customer_id: str, items: list, payment_method: str, discount: float = 0.0):
    # Step 1: Validate input
    if not customer_id or not customer_id.strip():
        return "Error: customer_id is required"
    if not items:
        return "Error: order must contain at least one item"

    # Step 2: Check stock
    for item in items:
        name, qty = item["name"], item["qty"]
        if name not in STOCK:
            return f"Error: '{name}' does not exist in catalogue"
        if STOCK[name] < qty:
            return f"Error: insufficient stock for '{name}' (requested {qty}, available {STOCK[name]})"

    # Step 3: Calculate subtotal
    subtotal = sum(item["qty"] * item["price"] for item in items)

    # Step 4: Apply discount
    if not (0.0 <= discount <= 1.0):
        return "Error: discount must be between 0.0 and 1.0"
    total = round(subtotal * (1 - discount), 2)

    # Step 5: Validate payment method
    if payment_method not in VALID_PAYMENT_METHODS:
        return f"Error: unknown payment method '{payment_method}'"

    # Step 6: Process payment (simulated — always succeeds here)
    payment_ok = True
    if not payment_ok:
        return "Error: payment failed"

    # Step 7: Deduct stock
    for item in items:
        STOCK[item["name"]] -= item["qty"]

    # Step 8: Return receipt
    return {
        "customer_id":    customer_id,
        "items":          items,
        "subtotal":       subtotal,
        "discount":       f"{int(discount * 100)}%",
        "total":          total,
        "payment_method": payment_method,
        "status":         "confirmed",
    }


# ─── TEST CASES ──────────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        # (description, args, expected_status)
        (
            "Valid order with discount",
            ("C001", [{"name": "Laptop", "qty": 1, "price": 999.99},
                      {"name": "Mouse",  "qty": 2, "price": 25.00}], "card", 0.1),
            "confirmed",
        ),
        (
            "Empty items list",
            ("C002", [], "card", 0.0),
            "Error",
        ),
        (
            "Out of stock",
            ("C003", [{"name": "Monitor", "qty": 100, "price": 300.00}], "cash", 0.0),
            "Error",
        ),
        (
            "Invalid payment method",
            ("C004", [{"name": "Keyboard", "qty": 1, "price": 49.99}], "bitcoin", 0.0),
            "Error",
        ),
    ]

    print(f"{'#':<4} {'Description':<35} {'Result'}")
    print("-" * 70)
    for i, (desc, args, expected) in enumerate(test_cases, 1):
        result = process_order(*args)
        if isinstance(result, dict):
            status = f"OK — total: ${result['total']}"
        else:
            status = result
        match = "PASS" if expected in str(result) else "FAIL"
        print(f"{i:<4} {desc:<35} [{match}] {status}")
