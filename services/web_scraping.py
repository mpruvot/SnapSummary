import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError, RequestException
from googlesearch import search

class WebScraper:
    def __init__(self) -> None:
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        self.soup: BeautifulSoup = None


    def fetch_google_search_urls(self, user_input: str, limit: int = 1):
        """
        Performs a Google search and returns a list of URLs as results.

        Args:
            user_input (str): The search query string.
            limit (int): Maximum number of search results to return (default is 1).

        Returns:
            List[str]: A list of URLs corresponding to the search results.
        """
        result = search(user_input, num_results=limit)
        return [r for r in result]


    def _make_request(self, url: str):
        """
        Makes an HTTP GET request to the specified URL.

        Args:
            url (str): The URL to which the GET request is made.

        Returns:
            requests.Response: The response object from the requests library.

        Raises:
            HTTPError: For HTTP-related errors.
            RequestException: For non-HTTP-related errors.
        """
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except RequestException as error:
            print(f"Other error occurred: {error}")
        
    def parse_html(self, html_content):
        """
        Parses HTML content using BeautifulSoup.

        Args:
            html_content (str): HTML content to be parsed.

        Returns:
            BeautifulSoup: Parsed HTML content.
        """
        self.soup = BeautifulSoup(html_content, 'html.parser')
        return self.soup
    