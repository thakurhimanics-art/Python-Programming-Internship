# Hard Level Tasks - Python Programming Internship

This folder contains advanced beginner projects demonstrating data persistence, state tracking, HTTP networking, DOM parsing, and ethical web scraping best practices.

---

## Table of Tasks

| Task | Program Name | Key Concepts | File Path |
| :--- | :--- | :--- | :--- |
| **Task 1** | To-Do List Manager | JSON persistence, CRUD state lifecycle, task indexing | `task1_todo_list/todo_list.py` |
| **Task 2** | Ethical Web Scraper | `requests`, `BeautifulSoup4`, HTTP status validation, timeouts, DOM parsing | `task2_web_scraper/web_scraper.py` |

---

## 1. Task 1: Command-Line To-Do List

### Description
A practical task manager that stores tasks in `todo_items.json`. Users can create tasks, review status flags (`[✓] Completed` or `[ ] Pending`), mark tasks as complete, and delete completed or unwanted items.

### Features
- **Persistent Storage:** Saves tasks to `todo_items.json` after every operation.
- **Input Validation:** Prevents blank task entries and validates 1-based index selections.
- **Timestamp Tracking:** Automatically records creation date and time for each task.

### Run Command (PowerShell)
```powershell
python hard/task1_todo_list/todo_list.py
```

### Example Input/Output
```text
=======================================================
                    TO-DO LIST                  
=======================================================
  1. [✓] Completed | Review Python internship syllabus (Added: 2026-10-22 19:40)
  2. [ ] Pending   | Run unit test suite (Added: 2026-10-22 19:40)
-------------------------------------------------------
 Total: 2 | Completed: 1 | Pending: 1
=======================================================
```

---

## 2. Task 2: Ethical Web Scraper

### Description
Demonstrates how to fetch and parse live HTML from the web using `requests` and `BeautifulSoup4`. The application targets public sandboxes designed for educational scraping (e.g. `https://quotes.toscrape.com/`).

### Ethical Scraping Guidelines
- **Educational Sandbox:** Uses `quotes.toscrape.com`, an open sandbox explicitly maintained for scrapers and automated parsers.
- **Custom User-Agent:** Sends a transparent, identifying User-Agent header rather than mimicking human browsers maliciously.
- **Timeouts & Rate Limiting:** Implements request timeouts (10 seconds) to prevent frozen connections.
- **HTTP Status Check:** Uses `response.raise_for_status()` to cleanly catch 404, 403, and 500 status codes.
- **Zero Scraping of Private Data:** Never targets authenticated portals, personal data, or pages disallowed by `robots.txt`.

### Dependencies
Requires `requests` and `beautifulsoup4`:
```powershell
pip install -r requirements.txt
```

### Run Command (PowerShell)
```powershell
python hard/task2_web_scraper/web_scraper.py
```

### Example Input/Output
```text
Requesting: https://quotes.toscrape.com/ ...

=================================================================
                  WEB SCRAPING RESULTS                   
=================================================================
Page Title : Quotes to Scrape
Source URL : https://quotes.toscrape.com/

--- Extracted Headings ---
 • <h1> Quotes to Scrape

--- Extracted Quotes Sample ---
 • "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking." - Albert Einstein
 • "It is our choices, Harry, that show what we truly are, far more than our abilities." - J.K. Rowling
 • "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle." - Albert Einstein
=================================================================
```
