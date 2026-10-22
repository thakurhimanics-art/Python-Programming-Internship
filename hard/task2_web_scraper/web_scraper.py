"""
Task 2: Ethical Web Scraper
Author: Himani Thakur
Description:
    Demonstrates ethical web scraping using requests and BeautifulSoup.
    Extracts page title, headings, quotes, and links with custom User-Agent headers,
    configurable request timeouts, and comprehensive network error handling.

Public Sandbox Target:
    Default target is 'https://quotes.toscrape.com/', an open educational sandbox
    specifically designed for practicing web scraping legally and ethically.
"""

import sys
import requests
from bs4 import BeautifulSoup

DEFAULT_DEMO_URL = "https://quotes.toscrape.com/"
DEFAULT_TIMEOUT = 10
CUSTOM_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) PythonInternshipDemo/1.0 (Educational Scraping)"
}


def fetch_page(url: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    """
    Fetch the raw HTML content of a URL with error handling and timeout.

    Parameters:
        url (str): Target web address.
        timeout (int): Maximum time in seconds to wait for server response.

    Returns:
        str: Raw HTML response text.

    Raises:
        ValueError: If URL format is invalid.
        requests.exceptions.RequestException: For connection, timeout, or HTTP errors.
    """
    url_clean = url.strip()
    if not (url_clean.startswith("http://") or url_clean.startswith("https://")):
        raise ValueError("Invalid URL scheme. The URL must begin with 'http://' or 'https://'.")

    response = requests.get(url_clean, headers=CUSTOM_HEADERS, timeout=timeout)
    response.raise_for_status()  # Raises HTTPError for 4xx or 5xx codes
    return response.text


def parse_html(html_content: str) -> dict:
    """
    Parse HTML string and extract meaningful structured elements.

    Extracts:
        - Page title (<title>)
        - Headings (<h1>, <h2>)
        - Quotes and authors (if available on quotes sandboxes)
        - Hyperlinks (<a> href and text)
    """
    if not html_content or not html_content.strip():
        return {
            "title": "Empty Document",
            "headings": [],
            "quotes": [],
            "links": [],
        }

    soup = BeautifulSoup(html_content, "html.parser")

    # 1. Extract Page Title
    title = soup.title.string.strip() if (soup.title and soup.title.string) else "No Title Found"

    # 2. Extract Headings (h1 and h2)
    headings = []
    for tag in soup.find_all(["h1", "h2"]):
        heading_text = tag.get_text(strip=True)
        if heading_text:
            headings.append(f"<{tag.name}> {heading_text}")

    # 3. Extract Quotes if present (e.g. quotes.toscrape.com structure)
    quotes = []
    quote_blocks = soup.find_all("div", class_="quote")
    for block in quote_blocks[:5]:  # limit to first 5
        text_elem = block.find("span", class_="text")
        author_elem = block.find("small", class_="author")
        text = text_elem.get_text(strip=True) if text_elem else ""
        # Clean unicode smart quotes for clean terminal output across platforms
        text = text.replace("\u201c", '"').replace("\u201d", '"').replace("\u2018", "'").replace("\u2019", "'")
        author = author_elem.get_text(strip=True) if author_elem else "Unknown"
        if text:
            quotes.append({"quote": text, "author": author})

    # 4. Extract sample links
    links = []
    for a in soup.find_all("a", href=True)[:5]:
        anchor_text = a.get_text(strip=True) or "[No Label]"
        links.append({"text": anchor_text, "href": a["href"]})

    return {
        "title": title,
        "headings": headings,
        "quotes": quotes,
        "links": links,
    }


def scrape_website(url: str, timeout: int = DEFAULT_TIMEOUT) -> dict:
    """Fetch and parse content from a live URL."""
    html = fetch_page(url, timeout=timeout)
    data = parse_html(html)
    data["source_url"] = url
    return data


def display_scraped_data(data: dict):
    """Print the parsed web scraping results clearly."""
    print("\n" + "=" * 65)
    print("                  WEB SCRAPING RESULTS                   ")
    print("=" * 65)
    print(f"Page Title : {data.get('title', 'N/A')}")
    if "source_url" in data:
        print(f"Source URL : {data['source_url']}")

    print("\n--- Extracted Headings ---")
    headings = data.get("headings", [])
    if headings:
        for h in headings[:10]:
            print(f" - {h}")
    else:
        print(" (No major headings found)")

    quotes = data.get("quotes", [])
    if quotes:
        print("\n--- Extracted Quotes Sample ---")
        for q in quotes:
            print(f' - "{q["quote"]}" - {q["author"]}')

    links = data.get("links", [])
    if links:
        print("\n--- Extracted Links Sample ---")
        for link in links:
            print(f" - {link['text']} -> {link['href']}")

    print("=" * 65 + "\n")


def main():
    print("=" * 65)
    print("            ETHICAL PYTHON WEB SCRAPER                   ")
    print("=" * 65)
    print("Demonstrates HTTP requests, status handling, and HTML parsing")
    print("using 'requests' and 'BeautifulSoup4'.\n")
    print(f"Default public sandbox: {DEFAULT_DEMO_URL}")

    while True:
        target = input("\nEnter URL (press Enter for default sandbox, 'q' to quit): ").strip()
        if target.lower() in ("q", "quit", "exit"):
            print("Exiting Web Scraper. Goodbye!")
            break

        url_to_scrape = target if target else DEFAULT_DEMO_URL

        print(f"\nRequesting: {url_to_scrape} ...")
        try:
            results = scrape_website(url_to_scrape)
            display_scraped_data(results)
        except requests.exceptions.HTTPError as err:
            print(f"[HTTP Error] Server responded with error: {err}")
        except requests.exceptions.ConnectionError:
            print("[Connection Error] Failed to connect to server. Check your internet connection or URL.")
        except requests.exceptions.Timeout:
            print(f"[Timeout Error] Request timed out after {DEFAULT_TIMEOUT} seconds.")
        except ValueError as err:
            print(f"[URL Error] {err}")
        except Exception as e:
            print(f"[Unexpected Error] {e}")

        again = input("Scrape another page? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
