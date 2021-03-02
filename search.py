from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')  # Locators

    URL = 'https://duckduckgo.com/'

    def __init__(self, browser):  # constructor init will be called frst
        self.browser = browser

    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)  # get - loads a given URL in the browser

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)  # *expand tuples into positional arguments
        search_input.send_keys(phrase + Keys.RETURN)

# For pressing Enter key over a textbox we can pass Keys.ENTER or Keys.RETURN to the sendKeys method for that
# textbox.
