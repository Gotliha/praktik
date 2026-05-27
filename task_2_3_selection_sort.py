# Task 2.3 - Selection Sort: Student Rating
# Sort students by average grade from highest to lowest.
# No built-in sort() or sorted() allowed.


def create_rating(students: list) -> list:
    result = [s for s in students]  # copy to avoid mutating original

    for i in range(len(result)):
        max_idx = i
        for j in range(i + 1, len(result)):
            if result[j][1] > result[max_idx][1]:
                max_idx = j
        result[i], result[max_idx] = result[max_idx], result[i]

    return result


# --- Demo ---
if __name__ == "__main__":
    students = [
        ("Alice",   88.5),
        ("Bob",     76.0),
        ("Charlie", 92.3),
        ("Diana",   88.5),
        ("Eve",     61.8),
        ("Frank",   95.1),
    ]

    rating = create_rating(students)

    print(f"{'Rank':<6} {'Name':<10} {'Avg Grade'}")
    print("-" * 28)
    for rank, (name, grade) in enumerate(rating, start=1):
        print(f"{rank:<6} {name:<10} {grade}")
