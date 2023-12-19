# test_webscraper.py
import pytest
from unittest.mock import patch
import requests

from services.web_scraping import WebScraper
  # Make sure this import path is correct

# Fixture to initialize an instance of WebScraper
@pytest.fixture
def scraper():
    return WebScraper()

# Fixture to mock the results returned by the google search
@pytest.fixture
def mock_google_search_results():
    return ['https://test.com', 'https://coucou.org', 'https://hello.net']

# Test for fetch_google_search_urls method
@patch('services.web_scraping.search')  # Mocking the 'search' function from 'googlesearch' library
def test_fetch_google_search_urls(mock_search, scraper, mock_google_search_results):
    mock_search.return_value = mock_google_search_results
    results = scraper.fetch_google_search_urls("test query", limit=3)
    assert results == mock_google_search_results  # Check if results match the mock
    mock_search.assert_called_with("test query", num_results=3)  # Ensure the mock was called correctly

# Fixture to simulate a successful response from requests.get
@pytest.fixture
def mock_requests_get_success():
    mocked_response = requests.Response()
    mocked_response.status_code = 200
    mocked_response._content = b'Success'
    return mocked_response

# Test for _make_request method with a successful HTTP request
@patch('requests.get')  # Mocking 'requests.get' to simulate HTTP requests
def test_make_request_success(mocked_get, mock_requests_get_success, scraper):
    mocked_get.return_value = mock_requests_get_success
    response = scraper._make_request('http://example.com')
    assert response.status_code == 200  # Check if status code is 200
    assert response.text == 'Success'  # Check if the response content is 'Success'

# Test for _make_request method with a failed HTTP request
@patch('requests.get')
def test_make_request_failure(mocked_get, scraper):
    mocked_get.side_effect = requests.exceptions.HTTPError("An error occurred")
    response = scraper._make_request('http://badurl.com')
    assert response is None  # The response should be None due to the HTTP error

# Test for parse_html method
def test_parse_html(scraper):
    html_content = "<html><head><title>Test</title></head><body></body></html>"
    soup = scraper.parse_html(html_content)
    assert soup.title.string == "Test"  # Check if the title of the parsed HTML is 'Test'
