# Task 2.4 - Stack: Bracket Validator
# Check if brackets (), [], {} are correctly balanced in code.
# All other characters are ignored.


def validate_brackets(code: str) -> bool:
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for ch in code:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()

    return len(stack) == 0


# --- Demo ---
if __name__ == "__main__":
    test_cases = [
        ("if (x > 0) { print(x) }",          True),
        ("def foo(a, b): return [a, (b+1)]",  True),
        ("x = {1: [2, (3 + 4)]}",             True),
        ("(((",                                False),
        ("{[}]",                               False),
        ("func(a, b]",                         False),
        ("",                                   True),
    ]

    for code, expected in test_cases:
        result = validate_brackets(code)
        status = "OK" if result == expected else "FAIL"
        print(f"[{status}] {repr(code)[:40]:<42} -> {result}")
