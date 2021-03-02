from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')

    SEARCH_INPUT = (By.ID, 'search_form_input')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        # List comprehension offers a shorter syntax when you want to create a new list based on the values of an
        # existing list.
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')  # getting the value from search
        return value

    def title(self):
        return self.browser.title
