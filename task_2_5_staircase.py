# Task 2.5 - Staircase Problem: Recursive vs Iterative
# Count the number of ways to climb n stairs (1 or 2 steps at a time).
# Compare performance for n = 10, 20, 30, 35.

import time


def climb_recursive(n: int) -> int:
    if n <= 1:
        return 1
    return climb_recursive(n - 1) + climb_recursive(n - 2)


def climb_iterative(n: int) -> int:
    if n <= 1:
        return 1
    prev, curr = 1, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


# --- Demo ---
if __name__ == "__main__":
    test_values = [10, 20, 30, 35]

    print(f"{'n':<6} {'Ways':<15} {'Recursive (s)':<18} {'Iterative (s)':<18}")
    print("-" * 60)

    for n in test_values:
        # Iterative (always fast)
        t0 = time.perf_counter()
        ways = climb_iterative(n)
        iter_time = time.perf_counter() - t0

        # Recursive (exponential)
        t0 = time.perf_counter()
        climb_recursive(n)
        rec_time = time.perf_counter() - t0

        print(f"{n:<6} {ways:<15} {rec_time:<18.6f} {iter_time:<18.6f}")

    print()
    print("Conclusion:")
    print("  Recursive: O(2^n) — doubles call tree each step, very slow for n>30.")
    print("  Iterative: O(n)   — just two variables, always instant.")
