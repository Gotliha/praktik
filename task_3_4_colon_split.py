# Task 3.4 - Count Elements by Colon Delimiter
# Count how many elements are separated by ':' in a string.


def count_colon_elements(s: str) -> int:
    if not s:
        return 0
    count = 1
    for ch in s:
        if ch == ':':
            count += 1
    return count


# --- Demo ---
if __name__ == "__main__":
    test_cases = [
        "one:two:three",
        "a:b:c:d:e",
        "no colons here",
        "single:",
        ":leading",
        "",
        ":::",
    ]

    for s in test_cases:
        print(f"'{s}' -> {count_colon_elements(s)} element(s)")
