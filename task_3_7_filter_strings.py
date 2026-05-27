# Task 3.7 - Filter Strings Longer Than 3 Characters
# Return only strings whose length is strictly greater than 3.


def filter_long_strings(strings: list) -> list:
    result = []
    for s in strings:
        if len(s) > 3:
            result.append(s)
    return result


# --- Demo ---
if __name__ == "__main__":
    test_cases = [
        ["hi", "hello", "ok", "yes", "code", "go", "python"],
        ["a", "ab", "abc", "abcd", "abcde"],
        [],
        ["cat", "dogs", "ox", "elephant"],
    ]

    for words in test_cases:
        filtered = filter_long_strings(words)
        print(f"Input    : {words}")
        print(f"Filtered : {filtered}")
        print()
