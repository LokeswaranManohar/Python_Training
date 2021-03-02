"""
These tests cover DuckDuckGo searches.
"""
import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('PHRASE', ['panda', 'python', 'polar bear'])  # run parallel
def test_basic_duckduckgo_search(browser, PHRASE):
    # def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # PHRASE = "Royal Enfield"

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(PHRASE)

    # Then the search result title contains "panda"
    # assert PHRASE in result_page.title()  # Race condition

    # Then the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

    # And the search result title contains "panda"
    assert PHRASE in result_page.title()  # Race condition
