"""
Task 3: Multiplication Table Generator
Author: Himani Thakur
Description:
    Generates and prints the multiplication table for any given number
    from 1 up to a specified limit (default: 1 to 10) using a for loop.
"""


def generate_table(number: int, limit: int = 10) -> list[str]:
    """
    Generate a formatted multiplication table for a given number.
    Returns a list of formatted equation strings.
    """
    table_lines = []
    for i in range(1, limit + 1):
        product = number * i
        table_lines.append(f"{number} x {i:2d} = {product}")
    return table_lines


def print_table(number: int, limit: int = 10):
    """Print the multiplication table with a header and separator."""
    print("\n" + "-" * 25)
    print(f" Multiplication Table for {number}")
    print("-" * 25)
    for line in generate_table(number, limit):
        print(f"  {line}")
    print("-" * 25)


def main():
    print("=" * 45)
    print("     MULTIPLICATION TABLE GENERATOR          ")
    print("=" * 45)

    while True:
        user_input = input("\nEnter a number (or 'q' to quit): ").strip()
        if user_input.lower() in ("q", "quit", "exit"):
            print("Exiting Multiplication Table Generator. Goodbye!")
            break

        try:
            num = int(user_input)
            print_table(num, limit=10)
        except ValueError:
            print("[Error] Please enter a valid integer.")

        again = input("\nGenerate another table? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
