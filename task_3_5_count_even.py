# Task 3.5 - Count Even Numbers in Array
# Accept an array of numbers and return the count of even elements.


def count_even(*numbers) -> int:
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count


# --- Demo ---
if __name__ == "__main__":
    test_cases = [
        (1, 2, 3, 4, 5, 6),
        (7, 9, 11, 13),
        (2, 4, 6, 8, 10),
        (0, -2, -4, 3),
        (),
    ]

    for nums in test_cases:
        print(f"Input: {nums}  ->  even count: {count_even(*nums)}")
