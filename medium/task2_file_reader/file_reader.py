"""
Task 2: File Reader
Author: Himani Thakur
Description:
    Reads and displays the contents of a UTF-8 encoded text file with robust
    error handling for non-existent files, encoding issues, and permission errors.
    Displays file statistics such as line count, word count, and byte size.
"""

import os


def read_file_content(filepath: str, encoding: str = "utf-8") -> str:
    """
    Read and return the contents of a text file.

    Parameters:
        filepath (str): Path to the target file.
        encoding (str): Text encoding (default: 'utf-8').

    Returns:
        str: File content.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IsADirectoryError: If the specified path points to a directory.
        PermissionError: If read permissions are lacking.
        UnicodeDecodeError: If decoding fails with the specified encoding.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: '{filepath}'")

    if os.path.isdir(filepath):
        raise IsADirectoryError(f"Target path is a directory, not a file: '{filepath}'")

    with open(filepath, mode="r", encoding=encoding) as file:
        return file.read()


def get_file_stats(content: str) -> dict:
    """Compute line count, word count, and character count of content string."""
    lines = content.splitlines()
    words = content.split()
    return {
        "line_count": len(lines),
        "word_count": len(words),
        "char_count": len(content),
    }


def main():
    print("=" * 50)
    print("                PYTHON FILE READER               ")
    print("=" * 50)

    # Determine default sample.txt path located in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    default_sample = os.path.join(script_dir, "sample.txt")

    while True:
        print(f"\nDefault sample file available: {os.path.basename(default_sample)}")
        user_path = input("Enter path to file (press Enter to open default sample, 'q' to quit): ").strip()

        if user_path.lower() in ("q", "quit", "exit"):
            print("Exiting File Reader. Goodbye!")
            break

        target_file = user_path if user_path else default_sample

        try:
            content = read_file_content(target_file)
            stats = get_file_stats(content)

            print("\n" + "=" * 50)
            print(f"File: {os.path.abspath(target_file)}")
            print(f"Stats: {stats['line_count']} lines | {stats['word_count']} words | {stats['char_count']} chars")
            print("=" * 50)
            print(content)
            print("=" * 50)

        except FileNotFoundError:
            print(f"\n[Error] The file '{target_file}' does not exist. Please check the path.")
        except PermissionError:
            print(f"\n[Error] Permission denied when attempting to read '{target_file}'.")
        except UnicodeDecodeError:
            print(f"\n[Error] Failed to decode '{target_file}'. The file may not be valid UTF-8.")
        except Exception as e:
            print(f"\n[Error] An unexpected error occurred: {e}")

        again = input("\nRead another file? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
