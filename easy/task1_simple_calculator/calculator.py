"""
Task 1: Simple Calculator
Author: Himani Thakur
Description:
    A beginner-friendly command-line calculator that supports addition,
    subtraction, multiplication, and division with error handling for
    invalid inputs and division by zero.
"""


def add(num1: float, num2: float) -> float:
    """Return the sum of two numbers."""
    return num1 + num2


def subtract(num1: float, num2: float) -> float:
    """Return the difference of two numbers."""
    return num1 - num2


def multiply(num1: float, num2: float) -> float:
    """Return the product of two numbers."""
    return num1 * num2


def divide(num1: float, num2: float) -> float:
    """Return the quotient of two numbers. Raises ValueError on division by zero."""
    if num2 == 0:
        raise ValueError("Error: Division by zero is undefined.")
    return num1 / num2


def calculate(num1: float, num2: float, operation: str) -> float:
    """
    Perform arithmetic calculation based on the operation symbol or choice.
    Supported operations: '+', '-', '*', '/' or '1', '2', '3', '4'.
    """
    op = operation.strip().lower()
    if op in ("+", "1", "add", "addition"):
        return add(num1, num2)
    elif op in ("-", "2", "subtract", "subtraction"):
        return subtract(num1, num2)
    elif op in ("*", "3", "multiply", "multiplication", "x"):
        return multiply(num1, num2)
    elif op in ("/", "4", "divide", "division"):
        return divide(num1, num2)
    else:
        raise ValueError(f"Invalid operation '{operation}'. Choose +, -, *, or /.")


def main():
    print("=" * 45)
    print("           SIMPLE PYTHON CALCULATOR          ")
    print("=" * 45)

    while True:
        try:
            print("\nSelect an operation:")
            print("  1. Addition (+)")
            print("  2. Subtraction (-)")
            print("  3. Multiplication (*)")
            print("  4. Division (/)")
            print("  5. Exit")

            choice = input("\nEnter choice (1-5 or +, -, *, /): ").strip()
            if choice in ("5", "exit", "quit", "q"):
                print("Thank you for using Simple Calculator. Goodbye!")
                break

            val1 = float(input("Enter first number: "))
            val2 = float(input("Enter second number: "))

            result = calculate(val1, val2, choice)
            # Display integer format if result has no decimal portion
            formatted_res = int(result) if result.is_integer() else round(result, 4)
            print(f"\n>>> Result: {formatted_res}")

        except ValueError as err:
            print(f"\n[Input Error]: {err}")
        except Exception as e:
            print(f"\n[Unexpected Error]: {e}")

        again = input("\nWould you like to perform another calculation? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Exiting calculator. Have a great day!")
            break


if __name__ == "__main__":
    main()
