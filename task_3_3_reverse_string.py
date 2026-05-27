# Task 3.3 - Reverse String
# Accept a string, store it, and print it in reverse order.


def reverse_string(s: str) -> str:
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result


# --- Demo ---
if __name__ == "__main__":
    test_strings = [
        "Hello, World!",
        "Python",
        "racecar",
        "  spaces  ",
        "",
    ]

    for s in test_strings:
        print(f"Original : '{s}'")
        print(f"Reversed : '{reverse_string(s)}'")
        print()
