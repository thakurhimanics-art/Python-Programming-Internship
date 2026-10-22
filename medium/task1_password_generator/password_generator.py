"""
Task 1: Secure Password Generator
Author: Himani Thakur
Description:
    Generates strong, cryptographically secure random passwords of customizable length.
    Each password is guaranteed to contain at least one uppercase letter, one lowercase
    letter, one digit, and one special character.

Security Note:
    Python's standard 'random' module is pseudo-random and predictable. For passwords
    and security tokens, the standard library 'secrets' module is used because it
    interfaces with the operating system's Cryptographically Secure Pseudo-Random
    Number Generator (CSPRNG).
"""

import secrets
import string

UPPERCASE_CHARS = string.ascii_uppercase
LOWERCASE_CHARS = string.ascii_lowercase
DIGIT_CHARS = string.digits
SPECIAL_CHARS = "!@#$%^&*()-_=+[]{}|;:,.<>?"
ALL_CHARS = UPPERCASE_CHARS + LOWERCASE_CHARS + DIGIT_CHARS + SPECIAL_CHARS


def generate_password(length: int = 12) -> str:
    """
    Generate a cryptographically secure random password of a given length.

    Parameters:
        length (int): Desired password length. Must be at least 4.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length is less than 4.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # Guarantee at least one character from each required category
    password_chars = [
        secrets.choice(UPPERCASE_CHARS),
        secrets.choice(LOWERCASE_CHARS),
        secrets.choice(DIGIT_CHARS),
        secrets.choice(SPECIAL_CHARS),
    ]

    # Fill the remaining length with random choices from the complete character set
    remaining_length = length - 4
    for _ in range(remaining_length):
        password_chars.append(secrets.choice(ALL_CHARS))

    # Cryptographically secure shuffle using SystemRandom
    secure_rng = secrets.SystemRandom()
    secure_rng.shuffle(password_chars)

    return "".join(password_chars)


def check_categories_present(password: str) -> bool:
    """Verify that password contains uppercase, lowercase, digit, and special characters."""
    has_upper = any(c in UPPERCASE_CHARS for c in password)
    has_lower = any(c in LOWERCASE_CHARS for c in password)
    has_digit = any(c in DIGIT_CHARS for c in password)
    has_special = any(c in SPECIAL_CHARS for c in password)
    return has_upper and has_lower and has_digit and has_special


def main():
    print("=" * 50)
    print("       CRYPTOGRAPHICALLY SECURE PASSWORD GENERATOR  ")
    print("=" * 50)
    print("Rules: Generates passwords with uppercase, lowercase,")
    print("       digits, and special symbols using Python 'secrets'.\n")

    while True:
        user_input = input("Enter desired password length (min 4, recommended 12-16) or 'q' to quit: ").strip()

        if user_input.lower() in ("q", "quit", "exit"):
            print("Exiting Password Generator. Goodbye!")
            break

        try:
            length = int(user_input)
            password = generate_password(length)
            print("\n" + "-" * 40)
            print(f"Generated Password : {password}")
            print(f"Password Length    : {len(password)}")
            print(f"Character Diversity: [Yes] Uppercase [Yes] Lowercase [Yes] Digit [Yes] Special")
            print("-" * 40 + "\n")
        except ValueError as err:
            print(f"[Error] {err}\n")

        again = input("Generate another password? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Stay safe and secure!")
            break


if __name__ == "__main__":
    main()
