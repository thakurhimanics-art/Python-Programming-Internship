"""
Task 4: Word Count Program
Author: Himani Thakur
Description:
    Accepts a sentence or text passage from the user and counts the total
    number of words using the split() method, with proper handling for
    empty inputs and extra whitespace.
"""


def count_words(text: str) -> int:
    """
    Count the number of words in a given string using split().
    Returns 0 if the text is empty or contains only whitespace.
    """
    if not text or not text.strip():
        return 0
    words = text.strip().split()
    return len(words)


def analyze_text(text: str) -> dict:
    """
    Provide basic text statistics: word count, character count (with/without spaces).
    """
    cleaned = text.strip() if text else ""
    words = cleaned.split() if cleaned else []
    return {
        "word_count": len(words),
        "char_count_total": len(text) if text else 0,
        "char_count_no_spaces": len("".join(words)) if words else 0,
    }


def main():
    print("=" * 45)
    print("           WORD COUNT PROGRAM                ")
    print("=" * 45)

    while True:
        sentence = input("\nEnter a sentence or paragraph (or 'q' to quit):\n> ").strip()

        if sentence.lower() in ("q", "quit", "exit"):
            print("Exiting Word Count Program. Goodbye!")
            break

        if not sentence:
            print("[Notice] You entered an empty sentence! Word count is 0.")
        else:
            stats = analyze_text(sentence)
            print("\n--- Text Statistics ---")
            print(f"Total Words          : {stats['word_count']}")
            print(f"Characters (no space): {stats['char_count_no_spaces']}")
            print(f"Characters (total)   : {stats['char_count_total']}")

        again = input("\nCount words in another sentence? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
