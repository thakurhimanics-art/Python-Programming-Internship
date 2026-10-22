"""
Unit Test Suite for Python Programming Internship Tasks
Author: Himani Thakur
Description:
    Comprehensive unit tests covering all 10 internship tasks across Easy,
    Medium, and Hard difficulty levels. Tests valid paths, edge cases,
    error conditions, data persistence, and security requirements.
"""

import os
import sys
import tempfile
import shutil
import unittest

# Ensure project root and task directories are on sys.path
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(TEST_DIR)

TASK_PATHS = [
    PROJECT_ROOT,
    os.path.join(PROJECT_ROOT, "easy", "task1_simple_calculator"),
    os.path.join(PROJECT_ROOT, "easy", "task2_number_guessing_game"),
    os.path.join(PROJECT_ROOT, "easy", "task3_multiplication_table"),
    os.path.join(PROJECT_ROOT, "easy", "task4_word_count"),
    os.path.join(PROJECT_ROOT, "medium", "task1_password_generator"),
    os.path.join(PROJECT_ROOT, "medium", "task2_file_reader"),
    os.path.join(PROJECT_ROOT, "medium", "task3_contact_book"),
    os.path.join(PROJECT_ROOT, "medium", "task4_file_organizer"),
    os.path.join(PROJECT_ROOT, "hard", "task1_todo_list"),
    os.path.join(PROJECT_ROOT, "hard", "task2_web_scraper"),
]

for p in TASK_PATHS:
    if p not in sys.path:
        sys.path.insert(0, p)

# Import module functions under test
from calculator import add, subtract, multiply, divide, calculate
from guessing_game import check_guess
from multiplication_table import generate_table
from word_count import count_words, analyze_text
from password_generator import (
    generate_password,
    check_categories_present,
    UPPERCASE_CHARS,
    LOWERCASE_CHARS,
    DIGIT_CHARS,
    SPECIAL_CHARS,
)
from file_reader import read_file_content, get_file_stats
from contact_book import (
    add_contact,
    search_contacts,
    update_contact,
    delete_contact,
    load_contacts,
    save_contacts,
)
from file_organizer import (
    get_category,
    get_safe_destination_path,
    is_safe_target_directory,
    organize_files,
)
from todo_list import (
    add_task,
    mark_complete,
    delete_task,
    load_tasks,
    save_tasks,
)
from web_scraper import parse_html, fetch_page, scrape_website


# =====================================================================
# EASY LEVEL TESTS
# =====================================================================

class TestEasyTask1Calculator(unittest.TestCase):
    """Unit tests for Task 1: Simple Calculator."""

    def test_arithmetic_operations(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(divide(20, 4), 5.0)

    def test_negative_and_decimal_numbers(self):
        self.assertAlmostEqual(add(-3.5, 1.2), -2.3)
        self.assertAlmostEqual(multiply(-4, -2.5), 10.0)

    def test_division_by_zero_raises_error(self):
        with self.assertRaises(ValueError) as ctx:
            divide(10, 0)
        self.assertIn("Division by zero", str(ctx.exception))

    def test_calculate_dispatcher(self):
        self.assertEqual(calculate(10, 2, "+"), 12)
        self.assertEqual(calculate(10, 2, "-"), 8)
        self.assertEqual(calculate(10, 2, "*"), 20)
        self.assertEqual(calculate(10, 2, "/"), 5.0)
        self.assertEqual(calculate(10, 2, "1"), 12)  # choice 1 is add

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculate(10, 2, "unknown_op")


class TestEasyTask2GuessingGame(unittest.TestCase):
    """Unit tests for Task 2: Number Guessing Game."""

    def test_check_guess_too_low(self):
        self.assertEqual(check_guess(25, 50), "Too Low")

    def test_check_guess_too_high(self):
        self.assertEqual(check_guess(75, 50), "Too High")

    def test_check_guess_correct(self):
        self.assertEqual(check_guess(50, 50), "Correct")


class TestEasyTask3MultiplicationTable(unittest.TestCase):
    """Unit tests for Task 3: Multiplication Table Generator."""

    def test_table_length_default(self):
        table = generate_table(7)
        self.assertEqual(len(table), 10)

    def test_table_values(self):
        table = generate_table(5, limit=3)
        self.assertEqual(len(table), 3)
        self.assertIn("5 x  1 = 5", table[0])
        self.assertIn("5 x  2 = 10", table[1])
        self.assertIn("5 x  3 = 15", table[2])

    def test_negative_multiplier(self):
        table = generate_table(-4, limit=2)
        self.assertIn("-4 x  1 = -4", table[0])
        self.assertIn("-4 x  2 = -8", table[1])


class TestEasyTask4WordCount(unittest.TestCase):
    """Unit tests for Task 4: Word Count Program."""

    def test_standard_sentence(self):
        text = "Antigravity AI is an extraordinary coding assistant"
        self.assertEqual(count_words(text), 7)

    def test_multiple_consecutive_spaces(self):
        text = "  Python    Programming    Internship   "
        self.assertEqual(count_words(text), 3)

    def test_empty_and_whitespace_only(self):
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("   \t\n   "), 0)

    def test_analyze_text_structure(self):
        stats = analyze_text("Hello World")
        self.assertEqual(stats["word_count"], 2)
        self.assertEqual(stats["char_count_total"], 11)
        self.assertEqual(stats["char_count_no_spaces"], 10)


# =====================================================================
# MEDIUM LEVEL TESTS
# =====================================================================

class TestMediumTask1PasswordGenerator(unittest.TestCase):
    """Unit tests for Task 1: Password Generator."""

    def test_default_and_custom_lengths(self):
        for length in [4, 8, 12, 20, 32]:
            pwd = generate_password(length)
            self.assertEqual(len(pwd), length)

    def test_character_categories_diversity(self):
        # Run across multiple samples to ensure all 4 character groups are present
        for _ in range(15):
            pwd = generate_password(16)
            self.assertTrue(check_categories_present(pwd), f"Password '{pwd}' missing required categories.")
            self.assertTrue(any(c in UPPERCASE_CHARS for c in pwd))
            self.assertTrue(any(c in LOWERCASE_CHARS for c in pwd))
            self.assertTrue(any(c in DIGIT_CHARS for c in pwd))
            self.assertTrue(any(c in SPECIAL_CHARS for c in pwd))

    def test_length_validation_rejects_under_4(self):
        with self.assertRaises(ValueError):
            generate_password(3)
        with self.assertRaises(ValueError):
            generate_password(0)


class TestMediumTask2FileReader(unittest.TestCase):
    """Unit tests for Task 2: File Reader."""

    def test_read_bundled_sample_file(self):
        sample_path = os.path.join(PROJECT_ROOT, "medium", "task2_file_reader", "sample.txt")
        self.assertTrue(os.path.exists(sample_path), "sample.txt must exist in task directory.")
        content = read_file_content(sample_path)
        self.assertIn("Python Programming Internship", content)

    def test_file_statistics_calculation(self):
        sample_text = "Line One\nLine Two with words\nLine Three"
        stats = get_file_stats(sample_text)
        self.assertEqual(stats["line_count"], 3)
        self.assertEqual(stats["word_count"], 8)
        self.assertEqual(stats["char_count"], len(sample_text))

    def test_file_not_found_handling(self):
        with self.assertRaises(FileNotFoundError):
            read_file_content("non_existent_file_internship_12345.txt")


class TestMediumTask3ContactBook(unittest.TestCase):
    """Unit tests for Task 3: Contact Book."""

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.storage_file = os.path.join(self.test_dir, "test_contacts.json")
        self.contacts = {}

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_add_valid_contact(self):
        success, msg = add_contact(self.contacts, "Himani", "+91 9876543210", "himani@example.com")
        self.assertTrue(success)
        self.assertIn("Himani", self.contacts)
        self.assertEqual(self.contacts["Himani"]["phone"], "+91 9876543210")

    def test_add_duplicate_contact_rejected(self):
        add_contact(self.contacts, "Rohan", "9876543210")
        success, msg = add_contact(self.contacts, "rohan", "9876543210")  # case-insensitive check
        self.assertFalse(success)
        self.assertIn("already exists", msg)

    def test_add_invalid_inputs(self):
        # Empty name
        success, msg = add_contact(self.contacts, "", "9876543210")
        self.assertFalse(success)

        # Invalid phone (< 7 digits)
        success, msg = add_contact(self.contacts, "Pooja", "123")
        self.assertFalse(success)

    def test_search_contact(self):
        add_contact(self.contacts, "Aarav Sharma", "+91 9876500000", "aarav@example.com")
        add_contact(self.contacts, "Kavita Rao", "+91 9123400000", "kavita@example.com")

        res_name = search_contacts(self.contacts, "aarav")
        self.assertEqual(len(res_name), 1)
        self.assertIn("Aarav Sharma", res_name)

        res_phone = search_contacts(self.contacts, "91234")
        self.assertEqual(len(res_phone), 1)
        self.assertIn("Kavita Rao", res_phone)

    def test_update_contact(self):
        add_contact(self.contacts, "Dev", "9876543210", "dev@old.com")
        success, msg = update_contact(self.contacts, "Dev", new_phone="9998887776", new_email="dev@new.com")
        self.assertTrue(success)
        self.assertEqual(self.contacts["Dev"]["phone"], "9998887776")
        self.assertEqual(self.contacts["Dev"]["email"], "dev@new.com")

    def test_delete_contact(self):
        add_contact(self.contacts, "UserToDelete", "9876543210")
        success, msg = delete_contact(self.contacts, "UserToDelete")
        self.assertTrue(success)
        self.assertNotIn("UserToDelete", self.contacts)

    def test_persistence_save_and_load(self):
        add_contact(self.contacts, "PersistUser", "9876543210", "persist@example.com")
        save_contacts(self.storage_file, self.contacts)

        reloaded = load_contacts(self.storage_file)
        self.assertIn("PersistUser", reloaded)
        self.assertEqual(reloaded["PersistUser"]["email"], "persist@example.com")


class TestMediumTask4FileOrganizer(unittest.TestCase):
    """Unit tests for Task 4: Safe File Organizer."""

    def setUp(self):
        # Create temporary disposable folder for testing
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_category_detection(self):
        self.assertEqual(get_category("photo.jpg"), "Images")
        self.assertEqual(get_category("document.pdf"), "Documents")
        self.assertEqual(get_category("clip.mp4"), "Videos")
        self.assertEqual(get_category("song.mp3"), "Audio")
        self.assertEqual(get_category("backup.zip"), "Archives")
        self.assertEqual(get_category("random_file.unknownext"), "Others")

    def test_safety_restriction_on_root_and_invalid(self):
        is_safe, _ = is_safe_target_directory("C:\\")
        self.assertFalse(is_safe)

        is_safe, _ = is_safe_target_directory("")
        self.assertFalse(is_safe)

    def test_dry_run_does_not_move_files(self):
        # Create dummy sample file
        dummy_file = os.path.join(self.test_dir, "notes.txt")
        with open(dummy_file, "w") as f:
            f.write("test content")

        actions = organize_files(self.test_dir, dry_run=True)
        self.assertEqual(len(actions), 1)
        self.assertEqual(actions[0]["category"], "Documents")
        # Ensure file is STILL in original place
        self.assertTrue(os.path.exists(dummy_file))
        # Ensure Documents directory was NOT created during dry run
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, "Documents")))

    def test_actual_organize_moves_files(self):
        # Create dummy files
        img = os.path.join(self.test_dir, "pic.png")
        doc = os.path.join(self.test_dir, "sheet.xlsx")
        with open(img, "w") as f:
            f.write("img")
        with open(doc, "w") as f:
            f.write("doc")

        actions = organize_files(self.test_dir, dry_run=False)
        self.assertEqual(len(actions), 2)

        # Verify moved to respective subfolders
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Images", "pic.png")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "Documents", "sheet.xlsx")))

    def test_name_collision_avoidance(self):
        cat_dir = os.path.join(self.test_dir, "Documents")
        os.makedirs(cat_dir, exist_ok=True)
        existing = os.path.join(cat_dir, "sample.txt")
        with open(existing, "w") as f:
            f.write("existing")

        safe_path = get_safe_destination_path(cat_dir, "sample.txt")
        self.assertTrue(safe_path.endswith("sample_1.txt"))


# =====================================================================
# HARD LEVEL TESTS
# =====================================================================

class TestHardTask1TodoList(unittest.TestCase):
    """Unit tests for Task 1: CLI To-Do List."""

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.storage_file = os.path.join(self.test_dir, "test_todo.json")
        self.tasks = []

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_add_task(self):
        success, msg = add_task(self.tasks, "Complete lab report")
        self.assertTrue(success)
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["title"], "Complete lab report")
        self.assertFalse(self.tasks[0]["completed"])

    def test_add_empty_task_rejected(self):
        success, msg = add_task(self.tasks, "   ")
        self.assertFalse(success)
        self.assertEqual(len(self.tasks), 0)

    def test_mark_complete(self):
        add_task(self.tasks, "Study Python")
        success, msg = mark_complete(self.tasks, 1)
        self.assertTrue(success)
        self.assertTrue(self.tasks[0]["completed"])

        # Marking again should notify already completed
        success2, msg2 = mark_complete(self.tasks, 1)
        self.assertFalse(success2)

    def test_delete_task(self):
        add_task(self.tasks, "Item 1")
        add_task(self.tasks, "Item 2")
        success, msg = delete_task(self.tasks, 1)
        self.assertTrue(success)
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0]["title"], "Item 2")

    def test_invalid_task_number(self):
        add_task(self.tasks, "Single Item")
        success, msg = mark_complete(self.tasks, 99)
        self.assertFalse(success)
        success_del, _ = delete_task(self.tasks, 0)
        self.assertFalse(success_del)

    def test_persistence_save_and_load(self):
        add_task(self.tasks, "Persistent Task 1")
        save_tasks(self.storage_file, self.tasks)

        reloaded = load_tasks(self.storage_file)
        self.assertEqual(len(reloaded), 1)
        self.assertEqual(reloaded[0]["title"], "Persistent Task 1")


class TestHardTask2WebScraper(unittest.TestCase):
    """Unit tests for Task 2: Web Scraper."""

    def test_parse_local_html_fixture(self):
        html_fixture = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Quotes Demonstration Sandbox</title>
        </head>
        <body>
            <h1>Main Title</h1>
            <h2>Subsection Heading</h2>
            <div class="quote">
                <span class="text">Simplicity is the soul of efficiency.</span>
                <small class="author">Austin Freeman</small>
            </div>
            <a href="https://example.com/about">About Us</a>
        </body>
        </html>
        """
        data = parse_html(html_fixture)
        self.assertEqual(data["title"], "Quotes Demonstration Sandbox")
        self.assertEqual(len(data["headings"]), 2)
        self.assertIn("<h1> Main Title", data["headings"])
        self.assertIn("<h2> Subsection Heading", data["headings"])
        self.assertEqual(len(data["quotes"]), 1)
        self.assertEqual(data["quotes"][0]["quote"], "Simplicity is the soul of efficiency.")
        self.assertEqual(data["quotes"][0]["author"], "Austin Freeman")
        self.assertEqual(len(data["links"]), 1)
        self.assertEqual(data["links"][0]["href"], "https://example.com/about")

    def test_parse_empty_html(self):
        data = parse_html("")
        self.assertEqual(data["title"], "Empty Document")
        self.assertEqual(data["headings"], [])
        self.assertEqual(data["quotes"], [])

    def test_invalid_url_scheme_raises_error(self):
        with self.assertRaises(ValueError):
            fetch_page("ftp://unsupported-scheme.com")

    def test_live_sandbox_if_connected(self):
        """Test live request to quotes.toscrape.com; skip if network is unavailable."""
        import requests
        try:
            results = scrape_website("https://quotes.toscrape.com/", timeout=5)
            self.assertIn("Quotes to Scrape", results["title"])
            self.assertTrue(len(results["quotes"]) > 0)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as err:
            self.skipTest(f"Skipping live network scrape test due to network limitation: {err}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
