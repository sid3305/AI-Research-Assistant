import requests

from app.utils.logger import logger
from bs4 import BeautifulSoup


class WebScraper:
    """
    Handles website text extraction.
    """

    def extract_text(self, url):
        """
        Download webpage and extract text.

        Args:
            url (str)

        Returns:
            dict
        """

        try:

            logger.info(
                f"Scraping URL: {url}"
            )
            
            headers = {
                "User-Agent":
                (
                    "Mozilla/5.0 "
                    "(Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 "
                    "(KHTML, like Gecko) "
                    "Chrome/124.0 Safari/537.36"
                )
            }

            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            title = soup.title.string if soup.title else "No Title"

            content = soup.find(
                "div",
                {"id": "mw-content-text"}
            )

            if content:
                text = content.get_text(
                    separator="\n",
                    strip=True
                )
            else:
                text = soup.get_text(
                    separator="\n",
                    strip=True
                )

            logger.info(
                f"Successfully scraped: {url}"
            )

            return {
                "title": title,
                "text": text
            }

        except requests.exceptions.RequestException as e:

            raise RuntimeError(
                f"Failed to scrape website: {e}"
            )