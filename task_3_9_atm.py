# Task 3.9 - ATM Simulator
# Functions: withdraw, deposit, check balance.
# Each operation validates its preconditions before executing.

WITHDRAWAL_LIMIT = 1000.00   # max single withdrawal


class ATM:
    def __init__(self, initial_balance: float = 0.0):
        self._balance = round(initial_balance, 2)

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> str:
        if amount <= 0:
            return f"Error: deposit amount must be positive (got {amount})"
        self._balance = round(self._balance + amount, 2)
        return f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}"

    def withdraw(self, amount: float) -> str:
        if amount <= 0:
            return f"Error: withdrawal amount must be positive (got {amount})"
        if amount > WITHDRAWAL_LIMIT:
            return f"Error: exceeds single withdrawal limit of ${WITHDRAWAL_LIMIT:.2f}"
        if amount > self._balance:
            return f"Error: insufficient funds (balance ${self._balance:.2f}, requested ${amount:.2f})"
        self._balance = round(self._balance - amount, 2)
        return f"Withdrawn ${amount:.2f}. New balance: ${self._balance:.2f}"

    def check_balance(self) -> str:
        return f"Current balance: ${self._balance:.2f}"


# --- Demo ---
if __name__ == "__main__":
    atm = ATM(initial_balance=500.00)
    print("=== ATM Simulator ===")
    print(atm.check_balance())
    print()

    operations = [
        ("deposit",  200.00),
        ("withdraw", 150.00),
        ("withdraw", 1500.00),   # over limit
        ("withdraw", 700.00),    # insufficient funds
        ("deposit",  -50.00),    # invalid amount
        ("withdraw", 0),         # invalid amount
        ("deposit",  300.00),
        ("withdraw", 999.99),
    ]

    for op, amount in operations:
        if op == "deposit":
            print(atm.deposit(amount))
        elif op == "withdraw":
            print(atm.withdraw(amount))

    print()
    print(atm.check_balance())
