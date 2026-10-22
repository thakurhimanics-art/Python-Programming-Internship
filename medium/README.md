# Medium Level Tasks - Python Programming Internship

This folder contains intermediate Python applications focusing on cryptography, file system operations, JSON data persistence, automation, and defensive programming.

---

## Table of Tasks

| Task | Program Name | Key Concepts | File Path |
| :--- | :--- | :--- | :--- |
| **Task 1** | Password Generator | Cryptographic randomness (`secrets`), string manipulation, character sets | `task1_password_generator/password_generator.py` |
| **Task 2** | File Reader | Safe file I/O (`with open`), UTF-8 encoding, error handling | `task2_file_reader/file_reader.py` |
| **Task 3** | Contact Book | CRUD operations, persistent JSON storage, input validation | `task3_contact_book/contact_book.py` |
| **Task 4** | File Organizer | File categorization, dry-run simulation, path collisions, `shutil` & `os` | `task4_file_organizer/file_organizer.py` |

---

## 1. Task 1: Password Generator

### Description
Generates strong, cryptographically secure passwords containing uppercase letters, lowercase letters, digits, and special characters.

### Why `secrets` is Used Over `random`
- **Mersenne Twister (`random` module):** Python's standard `random` module uses the Mersenne Twister PRNG. While fast and statistically uniform, it is completely deterministic. Given 624 observed outputs, an attacker can reconstruct internal state and predict future values. Therefore, `random` must never be used for security-sensitive data.
- **Operating System CSPRNG (`secrets` module):** The `secrets` module accesses cryptographically secure sources of entropy provided by the underlying OS (`CryptGenRandom` / `BCryptGenRandom` on Windows, `/dev/urandom` on Unix). Its output cannot be predicted even if previous outputs are known.
- **Guaranteed Category Presence:** The implementation guarantees that at least one uppercase letter, one lowercase letter, one digit, and one symbol are present in every password generated (length $\ge$ 4).

### Run Command (PowerShell)
```powershell
python medium/task1_password_generator/password_generator.py
```

### Example Input/Output
```text
Enter desired password length (min 4, recommended 12-16) or 'q' to quit: 14

----------------------------------------
Generated Password : k#9Wq$2Z!vP8mL
Password Length    : 14
Character Diversity: [✓] Uppercase [✓] Lowercase [✓] Digit [✓] Special
----------------------------------------
```

---

## 2. Task 2: File Reader

### Description
Opens and reads a UTF-8 encoded text file, displaying the contents along with line, word, and character metrics.

### Features
- Includes a ready-to-test demonstration file: `sample.txt`.
- Gracefully handles missing files (`FileNotFoundError`), folder paths instead of files (`IsADirectoryError`), encoding issues (`UnicodeDecodeError`), and permission denials.
- Uses Python's `with` context manager for leak-proof file descriptor management.

### Run Command (PowerShell)
```powershell
python medium/task2_file_reader/file_reader.py
```

### Example Input/Output
```text
Default sample file available: sample.txt
Enter path to file (press Enter to open default sample, 'q' to quit):

==================================================
File: .../medium/task2_file_reader/sample.txt
Stats: 13 lines | 68 words | 536 chars
==================================================
Python Programming Internship Sample Document
==============================================
Welcome to the Python File Reader demonstration!
...
```

---

## 3. Task 3: Contact Book

### Description
A persistent contact management system that stores contacts in `contacts.json`. Supports creating, viewing, searching, updating, and deleting contacts.

### Features
- **JSON Persistence:** Automatically saves modifications to `contacts.json`.
- **Fault Tolerance:** If the storage file is missing or contains malformed JSON, the application initializes safely with an empty dictionary instead of crashing.
- **Validation:** Rejects empty contact names, verifies that phone numbers contain sufficient digits, and prevents duplicate contact collisions.

### Run Command (PowerShell)
```powershell
python medium/task3_contact_book/contact_book.py
```

### Example Input/Output
```text
--- Main Menu ---
1. View All Contacts
2. Add New Contact
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter choice (1-6): 1

------------------------------------------------------------
Name                 | Phone              | Email             
----------------------------------------
Alice Sharma         | +91 98765 43210    | alice.sharma@example.com
Bob Patel            | +91 91234 56789    | bob.patel@example.com
------------------------------------------------------------
```

---

## 4. Task 4: File Organizer

### Description
Scans any user-specified folder and organizes loose files into categorized subfolders (`Images`, `Documents`, `Videos`, `Audio`, `Archives`, `Others`).

### Features & Safety Controls
- **Dry-Run Preview:** Simulates all actions first so the user can verify the proposed folder operations before any files are moved.
- **Root & System Guards:** Rejects root drives (`C:\`, `/`) and system directories to prevent unintended file disruption.
- **Conflict Avoidance:** If a file with the same name already exists in the destination folder, automatically appends a numeric suffix (e.g. `report_1.pdf`) rather than overwriting.
- **Directory Preservation:** Skips subdirectories and preserves the organizer script itself.

### Run Command (PowerShell)
```powershell
python medium/task4_file_organizer/file_organizer.py
```

### Example Input/Output
```text
Enter target folder path (or 'q' to quit): C:\temp\disposable_test

Analyzing directory: C:\temp\disposable_test

=================================================================
        FILE ORGANIZER SUMMARY [DRY-RUN PREVIEW]
=================================================================
 • [Documents] invoice.pdf -> Documents/invoice.pdf
 • [Images   ] photo.png -> Images/photo.png
 • [Archives ] project.zip -> Archives/project.zip
-----------------------------------------------------------------
Proposed to organize: 3 file(s).
=================================================================

Proceed with moving these files? (yes/no): yes
Files organized safely!
```
