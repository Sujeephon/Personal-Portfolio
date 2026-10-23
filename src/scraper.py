# web-scraping-intro/src/scraper.py
import requests
import json
import os
from bs4 import BeautifulSoup

class SimpleWebScraper:
    """
    A class to encapsulate basic web scraping functionality.
    """
    def __init__(self, target_url):
        self.target_url = target_url

    def _get_html_content(self):
        """
        Downloads the HTML content from the target URL.
        Handles basic error checking.
        """
        print(f"Downloading content from: {self.target_url}")
        try:
            # Add a User-Agent header to mimic a real browser, as some sites block default requests
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get(self.target_url, headers=headers, timeout=10)
            response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
            print("Successfully downloaded content.")
            return response.text
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e} - Status Code: {e.response.status_code}")
            return None
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error occurred: {e} - Could not connect to {self.target_url}")
            return None
        except requests.exceptions.Timeout:
            print("The request timed out.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"An unexpected request error occurred: {e}")
            return None

    def scrape_main_titles(self):
        """
        Scrapes the main book title and chapter titles from the Automate the Boring Stuff homepage.
        """
        html_content = self._get_html_content()
        if not html_content:
            return None

        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the main book title (site now just uses a plain <h1>)
        book_title_tag = soup.find('h1')
        book_title = book_title_tag.get_text(strip=True) if book_title_tag else "Book Title Not Found"

        # Extract chapter titles: chapter links point to URLs containing "/2e/chapter"
        chapter_titles = []
        for link in soup.select('a[href*="/2e/chapter"]'):
            title = link.get_text(strip=True)
            if title:
                chapter_titles.append(title)

        return {
            "book_title": book_title,
            "chapter_titles": chapter_titles
        }

    def save_to_json(self, data, output_path='data/scraped_output.json'):
        """
        Saves scraped data to a JSON file inside the data/ folder.
        Creates the folder if it doesn't already exist.
        """
        if not data:
            print("No data to save.")
            return

        # Create the data/ folder if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Data successfully saved to: {output_path}")
        except IOError as e:
            print(f"Error saving data to file: {e}")