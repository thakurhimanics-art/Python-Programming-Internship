# Easy Level Tasks - Python Programming Internship

This folder contains four beginner-friendly Python programs demonstrating fundamental programming concepts such as variables, arithmetic operators, conditional statements (`if-elif-else`), loops (`while`, `for`), functions, string manipulation, and input validation.

---

## Table of Tasks

| Task | Program Name | Key Concepts | File Path |
| :--- | :--- | :--- | :--- |
| **Task 1** | Simple Calculator | Functions, arithmetic operations, conditionals, division by zero handling | `task1_simple_calculator/calculator.py` |
| **Task 2** | Number Guessing Game | Random number generation, loops, comparison logic, input validation | `task2_number_guessing_game/guessing_game.py` |
| **Task 3** | Multiplication Table | `for` loops, formatted string printing, integer input handling | `task3_multiplication_table/multiplication_table.py` |
| **Task 4** | Word Count Program | String methods (`split()`, `strip()`), empty string checks, text stats | `task4_word_count/word_count.py` |

---

## 1. Task 1: Simple Calculator

### Description
Performs basic arithmetic calculations (addition, subtraction, multiplication, and division) on two numbers entered by the user.

### Features
- Menu-driven interface supporting symbols (`+`, `-`, `*`, `/`) or numbers (`1-4`).
- Handles `ZeroDivisionError` with an informative error message.
- Re-prompts the user to perform continuous calculations until they choose to exit.

### Run Command (PowerShell)
```powershell
python easy/task1_simple_calculator/calculator.py
```

### Example Input/Output
```text
Select an operation:
  1. Addition (+)
  2. Subtraction (-)
  3. Multiplication (*)
  4. Division (/)
  5. Exit

Enter choice (1-5 or +, -, *, /): 1
Enter first number: 25
Enter second number: 15

>>> Result: 40
```

---

## 2. Task 2: Number Guessing Game

### Description
Generates a random integer between 1 and 100. The user attempts to guess the number while the program provides hints indicating whether the guess is "Too High" or "Too Low".

### Features
- Uses Python's built-in `random.randint()`.
- Tracks and displays total attempts taken upon a successful guess.
- Validates user input to prevent crashes from non-numeric or out-of-range values.

### Run Command (PowerShell)
```powershell
python easy/task2_number_guessing_game/guessing_game.py
```

### Example Input/Output
```text
I have chosen a secret number between 1 and 100.
Can you guess what it is?

Enter your guess (1-100) or 'q' to quit: 50
📈 Too High! Try a lower number.

Enter your guess (1-100) or 'q' to quit: 25
📉 Too Low! Try a higher number.

Enter your guess (1-100) or 'q' to quit: 37
🎉 Congratulations! You guessed the number 37 correctly!
Total attempts taken: 3
```

---

## 3. Task 3: Multiplication Table Generator

### Description
Takes an integer from the user and outputs its multiplication table from 1 to 10 using a `for` loop.

### Features
- Formats output with clean column alignments.
- Modular `generate_table()` function returning a list of values for testability.
- Validates that the input is a valid integer.

### Run Command (PowerShell)
```powershell
python easy/task3_multiplication_table/multiplication_table.py
```

### Example Input/Output
```text
Enter a number (or 'q' to quit): 7

-------------------------
 Multiplication Table for 7
-------------------------
  7 x  1 = 7
  7 x  2 = 14
  7 x  3 = 21
  7 x  4 = 28
  7 x  5 = 35
  7 x  6 = 42
  7 x  7 = 49
  7 x  8 = 56
  7 x  9 = 63
  7 x 10 = 70
-------------------------
```

---

## 4. Task 4: Word Count Program

### Description
Accepts a sentence or paragraph and calculates the total word count using Python's `split()` method.

### Features
- Efficiently ignores redundant spaces between words.
- Handles empty or whitespace-only inputs without crashing.
- Provides additional text metrics: total characters and characters without spaces.

### Run Command (PowerShell)
```powershell
python easy/task4_word_count/word_count.py
```

### Example Input/Output
```text
Enter a sentence or paragraph (or 'q' to quit):
> Learning Python for software development is exciting and rewarding!

--- Text Statistics ---
Total Words          : 8
Characters (no space): 56
Characters (total)   : 63
```
