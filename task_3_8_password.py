# Task 3.8 - Password Input Mechanism
# Simulate a login system with attempt counting and lockout.
# Uses getpass so the typed password is hidden in the terminal.

import getpass

CORRECT_PASSWORD = "Secret123"
MAX_ATTEMPTS = 3


def enter_password() -> str:
    return getpass.getpass("Enter password: ")


def count_attempts(current: int) -> int:
    return current + 1


def is_locked(attempts: int, max_attempts: int) -> bool:
    return attempts >= max_attempts


def run_login():
    attempts = 0
    print("=== Login System ===")

    while not is_locked(attempts, MAX_ATTEMPTS):
        password = enter_password()
        attempts = count_attempts(attempts)

        if password == CORRECT_PASSWORD:
            print(f"Access granted! (attempt {attempts}/{MAX_ATTEMPTS})")
            return True
        else:
            remaining = MAX_ATTEMPTS - attempts
            if remaining > 0:
                print(f"Wrong password. {remaining} attempt(s) remaining.")
            else:
                print("Access blocked. Too many failed attempts.")
                return False

    return False


# --- Demo (non-interactive) for testing without a terminal ---
def simulate_login(passwords_to_try: list) -> str:
    attempts = 0
    for pwd in passwords_to_try:
        attempts = count_attempts(attempts)
        if pwd == CORRECT_PASSWORD:
            return f"Access granted on attempt {attempts}"
        if is_locked(attempts, MAX_ATTEMPTS):
            return "Access blocked after too many wrong attempts"
    return "Session ended without success"


if __name__ == "__main__":
    print("=== Simulation (non-interactive) ===")
    scenarios = [
        (["wrong", "Secret123"],                   "should succeed on 2nd try"),
        (["bad1", "bad2", "bad3"],                 "should be locked out"),
        (["Secret123"],                            "should succeed on 1st try"),
        (["x", "y", "Secret123", "never_reached"], "locked before correct"),
    ]

    for passwords, description in scenarios:
        result = simulate_login(passwords)
        print(f"  {description:<40} -> {result}")

    print()
    print("To run the interactive version, call run_login() in a terminal.")
