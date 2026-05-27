# Task 3.1 - Programming Paradigms Analysis
# Three languages from different paradigms demonstrated with the same task:
# calculate the sum of even numbers in a list.

# ─────────────────────────────────────────
# 1. Python — Multi-paradigm (OOP + functional + procedural)
#    Typing: dynamic, strong
#    Used for: web, data science, scripting, AI
# ─────────────────────────────────────────

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Procedural style
def sum_even_procedural(nums):
    total = 0
    for n in nums:
        if n % 2 == 0:
            total += n
    return total

# Functional style (Python)
sum_even_functional = sum(filter(lambda x: x % 2 == 0, numbers))

print("=== Python ===")
print(f"Procedural : {sum_even_procedural(numbers)}")
print(f"Functional : {sum_even_functional}")


# ─────────────────────────────────────────
# 2. Haskell-style (Pure Functional) — simulated in Python
#    Typing: static, strong (Hindley-Milner)
#    Used for: compilers, formal verification, finance
#
#    In Haskell this would be:
#      sumEven xs = sum (filter even xs)
#
#    Key traits: immutability, no side effects, lazy evaluation
# ─────────────────────────────────────────

from functools import reduce

haskell_style = reduce(lambda acc, x: acc + x if x % 2 == 0 else acc, numbers, 0)

print("\n=== Haskell-style (pure functional, simulated) ===")
print(f"Result: {haskell_style}")


# ─────────────────────────────────────────
# 3. Java-style (OOP) — simulated in Python
#    Typing: static, strong (nominal)
#    Used for: enterprise apps, Android, backend services
#
#    In Java this would be a class with methods.
#    Key traits: encapsulation, inheritance, polymorphism
# ─────────────────────────────────────────

class NumberAnalyzer:
    def __init__(self, numbers: list):
        self._numbers = numbers

    def sum_even(self) -> int:
        total = 0
        for n in self._numbers:
            if n % 2 == 0:
                total += n
        return total

print("\n=== Java-style OOP (simulated) ===")
analyzer = NumberAnalyzer(numbers)
print(f"Result: {analyzer.sum_even()}")


# ─────────────────────────────────────────
# Summary table
# ─────────────────────────────────────────
print("\n" + "=" * 60)
print(f"{'Language':<12} {'Paradigm':<20} {'Typing':<20} {'Use case'}")
print("-" * 60)
print(f"{'Python':<12} {'Multi-paradigm':<20} {'Dynamic/Strong':<20} {'AI, web, scripting'}")
print(f"{'Haskell':<12} {'Pure Functional':<20} {'Static/Strong':<20} {'Compilers, finance'}")
print(f"{'Java':<12} {'OOP':<20} {'Static/Strong':<20} {'Enterprise, Android'}")
