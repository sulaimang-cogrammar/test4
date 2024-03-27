"""
This module demonstrates different arithmetic operations.
"""

from arithmetic.add import add


def main():
    """The main implementation of this application."""
    # Demonstrate addition:
    a = 1
    b = 2
    print(f"{a} + {b} = {add(a, b)}")

    # Demonstrate subtraction:
    print(f"{a} - {b} = {a-b}")

    # Demonstrate multiplication:
    print(f"{a} * {b} = {a*b}")

    # Demonstrate division:


if __name__ == "__main__":
    main()
