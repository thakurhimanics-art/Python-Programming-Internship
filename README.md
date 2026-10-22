# Python Programming Internship Portfolio

> **Student Name:** Himani Thakur  
> **Course:** B.Tech Computer Science & Engineering (CSE)  
> **Repository:** Python-Programming-Internship  
> **Internship Track:** Python Programming Internship  
> **Python Version Tested:** Python 3.12.10 (Compatible with Python 3.10+)  

Welcome to my **Python Programming Internship** repository. This project is a curated compilation of **10 real-world Python applications** designed to showcase progressive mastery over fundamental, intermediate, and advanced practical programming concepts in Python.

---

## Project Structure Overview

```text
Python-Programming-Internship/
├── README.md                           # Main project documentation & execution guide
├── .gitignore                          # Standard Python & OS ignore rules
├── requirements.txt                    # External dependencies (requests, bs4)
├── easy/
│   ├── README.md                       # Easy-level overview and execution guide
│   ├── task1_simple_calculator/
│   │   └── calculator.py               # Arithmetic calculator with error handling
│   ├── task2_number_guessing_game/
│   │   └── guessing_game.py            # Random guessing game with feedback & score
│   ├── task3_multiplication_table/
│   │   └── multiplication_table.py     # Loop-driven formatted multiplication tables
│   └── task4_word_count/
│       └── word_count.py               # Text analyzer & word counter using split()
├── medium/
│   ├── README.md                       # Medium-level overview and security documentation
│   ├── task1_password_generator/
│   │   └── password_generator.py       # CSPRNG password generator using 'secrets'
│   ├── task2_file_reader/
│   │   ├── file_reader.py              # Robust UTF-8 file reader with statistics
│   │   └── sample.txt                  # Sample test text file
│   ├── task3_contact_book/
│   │   └── contact_book.py             # Persistent JSON CRUD contact book
│   └── task4_file_organizer/
│       └── file_organizer.py           # Automated file sorter with dry-run mode
├── hard/
│   ├── README.md                       # Hard-level overview and ethical scraping guide
│   ├── task1_todo_list/
│   │   └── todo_list.py                # Command-line To-Do manager with JSON persistence
│   └── task2_web_scraper/
│       └── web_scraper.py              # Ethical web scraper with bs4 & requests
└── tests/
    └── test_tasks.py                   # Automated unit test suite covering all 10 tasks
```

---

## Master Table of Internship Tasks

| Level | Task # | Task Name | Key Python Concepts | File Location |
| :--- | :---: | :--- | :--- | :--- |
| **Easy** | 1 | Simple Calculator | Arithmetic operators, conditionals (`if/elif/else`), zero division guard | [`easy/task1_simple_calculator/calculator.py`](easy/task1_simple_calculator/calculator.py) |
| **Easy** | 2 | Number Guessing Game | `random.randint()`, loops (`while`), attempt tracking, input bounds | [`easy/task2_number_guessing_game/guessing_game.py`](easy/task2_number_guessing_game/guessing_game.py) |
| **Easy** | 3 | Multiplication Table | `for` loops, range sequence, tabular string formatting | [`easy/task3_multiplication_table/multiplication_table.py`](easy/task3_multiplication_table/multiplication_table.py) |
| **Easy** | 4 | Word Count Program | String methods (`split()`, `strip()`), empty string checks, metrics | [`easy/task4_word_count/word_count.py`](easy/task4_word_count/word_count.py) |
| **Medium** | 1 | Password Generator | `secrets` module (CSPRNG), guaranteed character diversity, validation | [`medium/task1_password_generator/password_generator.py`](medium/task1_password_generator/password_generator.py) |
| **Medium** | 2 | File Reader | Context managers (`with open`), UTF-8 encoding, file stats, exception safety | [`medium/task2_file_reader/file_reader.py`](medium/task2_file_reader/file_reader.py) |
| **Medium** | 3 | Contact Book | JSON serialization, CRUD operations, persistent disk storage, phone validation | [`medium/task3_contact_book/contact_book.py`](medium/task3_contact_book/contact_book.py) |
| **Medium** | 4 | File Organizer | Extension categorizing, dry-run simulation, path collision safety, `shutil` | [`medium/task4_file_organizer/file_organizer.py`](medium/task4_file_organizer/file_organizer.py) |
| **Hard** | 1 | CLI To-Do List | State management, JSON persistence, status toggles, deletion by index | [`hard/task1_todo_list/todo_list.py`](hard/task1_todo_list/todo_list.py) |
| **Hard** | 2 | Ethical Web Scraper | `requests`, `BeautifulSoup4`, HTTP status checks, User-Agent, timeouts | [`hard/task2_web_scraper/web_scraper.py`](hard/task2_web_scraper/web_scraper.py) |

---

## Prerequisites and Installation

### 1. Python Version
Ensure that **Python 3.10+** (tested on **Python 3.12.10**) is installed and available in your environment:
```powershell
python --version
```

### 2. Clone the Repository
```powershell
git clone https://github.com/thakurhimanics-art/Python-Programming-Internship.git
cd Python-Programming-Internship
```

### 3. Install Dependencies
Tasks 1 through 9 use only Python's Standard Library. Task 10 (Web Scraper) utilizes `requests` and `beautifulsoup4`. Install dependencies via:
```powershell
pip install -r requirements.txt
```

---

## How to Run Every Task (Windows PowerShell)

All commands should be executed from the **root directory** (`Python-Programming-Internship/`):

### Easy Tasks
```powershell
# Task 1: Simple Calculator
python easy/task1_simple_calculator/calculator.py

# Task 2: Number Guessing Game
python easy/task2_number_guessing_game/guessing_game.py

# Task 3: Multiplication Table Generator
python easy/task3_multiplication_table/multiplication_table.py

# Task 4: Word Count Program
python easy/task4_word_count/word_count.py
```

### Medium Tasks
```powershell
# Task 1: Secure Password Generator
python medium/task1_password_generator/password_generator.py

# Task 2: File Reader
python medium/task2_file_reader/file_reader.py

# Task 3: Contact Book (Persistent)
python medium/task3_contact_book/contact_book.py

# Task 4: File Organizer (With Dry-Run Mode)
python medium/task4_file_organizer/file_organizer.py
```

### Hard Tasks
```powershell
# Task 1: Command-Line To-Do List
python hard/task1_todo_list/todo_list.py

# Task 2: Ethical Web Scraper
python hard/task2_web_scraper/web_scraper.py
```

---

## Detailed Task Descriptions & Input/Output Examples

### Task 1: Simple Calculator
- **Features:** Supports `+`, `-`, `*`, `/`. Implements custom checks for division by zero and rejects non-numeric input cleanly.
- **Example:**
  ```text
  Enter choice (1-5 or +, -, *, /): 4
  Enter first number: 50
  Enter second number: 0
  >>> [Input Error]: Error: Division by zero is undefined.
  ```

### Task 2: Number Guessing Game
- **Features:** Generates a random number in $[1, 100]$. Provides "Too High" or "Too Low" hints and reports total attempts upon success.
- **Example:**
  ```text
  Enter your guess (1-100) or 'q' to quit: 42
  📈 Too High! Try a lower number.
  Enter your guess (1-100) or 'q' to quit: 21
  🎉 Congratulations! You guessed the number 21 correctly!
  Total attempts taken: 2
  ```

### Task 3: Multiplication Table Generator
- **Features:** Takes any integer and outputs its multiplication table from 1 to 10 with neat formatting.
- **Example:**
  ```text
  Enter a number (or 'q' to quit): 9
  -------------------------
   Multiplication Table for 9
  -------------------------
    9 x  1 = 9
    9 x  2 = 18
    ...
    9 x 10 = 90
  -------------------------
  ```

### Task 4: Word Count Program
- **Features:** Uses `split()` to correctly parse words while ignoring multiple consecutive whitespace characters.
- **Example:**
  ```text
  Enter a sentence or paragraph (or 'q' to quit):
  > Antigravity AI pair programming enables rapid, clean software delivery.

  --- Text Statistics ---
  Total Words          : 8
  Characters (no space): 62
  Characters (total)   : 69
  ```

### Task 5: Password Generator
- **Features:** Employs `secrets` (OS-level CSPRNG) rather than `random`. Guarantees that at least one uppercase letter, one lowercase letter, one digit, and one special character are included in every valid password.
- **Example:**
  ```text
  Enter desired password length (min 4, recommended 12-16) or 'q' to quit: 12
  ----------------------------------------
  Generated Password : 8!pL9#wK$2Zm
  Password Length    : 12
  Character Diversity: [✓] Uppercase [✓] Lowercase [✓] Digit [✓] Special
  ----------------------------------------
  ```

### Task 6: File Reader
- **Features:** Safely reads UTF-8 files, handles `FileNotFoundError` gracefully, and calculates line, word, and character counts. Includes a default `sample.txt`.
- **Example:**
  ```text
  Enter path to file (press Enter to open default sample, 'q' to quit):
  Stats: 13 lines | 68 words | 536 chars
  ```

### Task 7: Contact Book
- **Features:** Persistent JSON storage in `contacts.json`. Validates phone numbers, avoids duplicate names, and supports searching across names, phones, and emails.
- **Example:**
  ```text
  1. View All Contacts
  2. Add New Contact
  3. Search Contact
  ...
  >>> Contact 'Aarav Mehta' added successfully.
  ```

### Task 8: Safe File Organizer
- **Features:** Organizes loose files into `Images`, `Documents`, `Videos`, `Audio`, `Archives`, and `Others`. Implements a dry-run preview, guards root and system drives, and automatically renames destination conflicts (`report_1.pdf`) to prevent data loss.
- **Example:**
  ```text
  =================================================================
          FILE ORGANIZER SUMMARY [DRY-RUN PREVIEW]
  =================================================================
   • [Documents] test_notes.txt -> Documents/test_notes.txt
   • [Images   ] graphic.png    -> Images/graphic.png
  -----------------------------------------------------------------
  Proposed to organize: 2 file(s).
  ```

### Task 9: Command-Line To-Do List
- **Features:** Stores tasks persistently in `todo_items.json`. Displays `[✓] Completed` and `[ ] Pending` indicators with creation timestamps.
- **Example:**
  ```text
  1. [✓] Completed | Review Python internship syllabus (Added: 2026-10-22 19:40)
  2. [ ] Pending   | Run unit test suite (Added: 2026-10-22 19:40)
  ```

### Task 10: Ethical Web Scraper
- **Features:** Scrapes `quotes.toscrape.com` (an educational sandbox). Sets a custom User-Agent, applies a 10-second timeout, verifies HTTP response status, and extracts titles, headings, and quotes.
- **Example:**
  ```text
  Requesting: https://quotes.toscrape.com/ ...
  Page Title : Quotes to Scrape
  Extracted Quotes:
   • "The world as we have created it..." - Albert Einstein
  ```

---

## Automated Unit Testing

All 10 applications are covered by an automated test suite using Python's standard `unittest` framework in [`tests/test_tasks.py`](tests/test_tasks.py).

### How to Run Tests
```powershell
python tests/test_tasks.py
```
Or via the unittest discovery tool:
```powershell
python -m unittest discover tests
```

### Coverage Scope:
- **Calculator:** Tests addition, subtraction, multiplication, division, zero division error, invalid operations.
- **Guessing Game:** Tests `check_guess()` for lower, higher, and correct matches.
- **Multiplication Table:** Tests line counts, products, and custom limits.
- **Word Count:** Tests standard sentences, multiple spaces, empty inputs, whitespace-only strings.
- **Password Generator:** Tests length constraints, guaranteed character sets (upper, lower, digit, special), and rejection of length $< 4$.
- **File Reader:** Tests reading existing files, line/word counting, and `FileNotFoundError` handling.
- **Contact Book:** Tests adding, searching, updating, deleting, input validation, and JSON serialization.
- **File Organizer:** Tests categorization logic, conflict renaming (`_1`), dry-run non-modification, and actual file moves inside an isolated temporary directory.
- **To-Do List:** Tests task creation, completion toggling, deletion, index validation, and JSON persistence.
- **Web Scraper:** Tests DOM parsing on local HTML fixture, title/heading extraction, empty HTML handling, and network error handling.

---

## GitHub Setup & Upload Instructions

Follow these steps to publish this repository to your GitHub account:

### Step 1: Initialize Git & Verify Changes
```powershell
git status
```

### Step 2: Commit Your Files
```powershell
git add .
git commit -m "feat: complete Python Programming Internship projects with unit tests and documentation"
```

### Step 3: Create GitHub Repository & Push
1. Open [GitHub](https://github.com/new) in your browser.
2. Create a new public repository named **`Python-Programming-Internship`** (do not initialize with README, license, or gitignore since we already have them).
3. Connect your local repository to GitHub and push:
```powershell
git remote add origin https://github.com/thakurhimanics-art/Python-Programming-Internship.git
git branch -M main
git push -u origin main
```

---

## Project Verification

All 10 applications are fully verified and accompanied by automated tests in `tests/test_tasks.py`. You can execute the test suite anytime using `python tests/test_tasks.py` to confirm that all test assertions and edge cases pass successfully.
