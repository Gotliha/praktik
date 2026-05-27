# Task 2.8 - Deque: Palindrome Checker
# Check if a phrase is a palindrome, ignoring spaces, punctuation and case.
# Custom Deque class (no collections.deque allowed).


class Deque:
    def __init__(self):
        self._items = []

    def add_front(self, item) -> None:
        self._items.insert(0, item)

    def add_rear(self, item) -> None:
        self._items.append(item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


def is_palindrome(phrase: str) -> bool:
    d = Deque()

    for ch in phrase.lower():
        if ch.isalnum():
            d.add_rear(ch)

    while d.size() > 1:
        if d.remove_front() != d.remove_rear():
            return False

    return True


# --- Demo ---
if __name__ == "__main__":
    test_cases = [
        "racecar",
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "No lemon no melon",
        "Hello World",
        "Not a palindrome",
        "Never odd or even",
    ]

    for phrase in test_cases:
        result = is_palindrome(phrase)
        label = "Palindrome    " if result else "Not palindrome"
        print(f"[{label}] '{phrase}'")
