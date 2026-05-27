# Task 3.6 - Sort Strings by Length
# Accept an array of strings and return them sorted by character count (ascending).
# Using insertion sort — no built-in sort() or sorted().


def sort_by_length(strings: list) -> list:
    result = strings[:]  # copy
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and len(result[j]) > len(key):
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


# --- Demo ---
if __name__ == "__main__":
    test_cases = [
        ["banana", "fig", "apple", "kiwi", "strawberry", "go"],
        ["python", "java", "c", "javascript", "go"],
        [],
        ["same", "size", "here"],
    ]

    for words in test_cases:
        print(f"Before : {words}")
        print(f"After  : {sort_by_length(words)}")
        print()
