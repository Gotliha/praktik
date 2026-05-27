# Task 2.2 - Binary Search: Electronic Dictionary
# Search a word in a sorted dictionary with O(log n) complexity.
# Returns the definition or "Word not found".


def search_dictionary(dictionary: list, word: str) -> str:
    low, high = 0, len(dictionary) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_word = dictionary[mid][0]

        if mid_word == word:
            return dictionary[mid][1]
        elif mid_word < word:
            low = mid + 1
        else:
            high = mid - 1

    return "Word not found"


# --- Demo ---
if __name__ == "__main__":
    dictionary = [
        ("Algorithm", "A step-by-step procedure for solving a problem"),
        ("Binary",    "Relating to a system of numbers with base 2"),
        ("Cache",     "Temporary storage for fast data access"),
        ("Debug",     "The process of finding and fixing errors in code"),
        ("Encrypt",   "Convert data into a coded form"),
        ("Function",  "A reusable block of code that performs a specific task"),
        ("Hash",      "A fixed-size value computed from input data"),
        ("Iterator",  "An object that allows traversal through a collection"),
    ]

    queries = ["Cache", "Function", "Python", "Algorithm"]
    for q in queries:
        print(f"'{q}': {search_dictionary(dictionary, q)}")
