import pytest
import time
import random
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

scenarios('../features/check_remove.feature')


@then('in result page click on random item and remove')
def result(browser):
    currenturl = browser.current_url
    randomNumber = random.randint(1, 6)
    if currenturl == 'https://www.saucedemo.com/inventory.html':
        # navigate = browser.find_element_by_xpath('//*[@id="inventory_container"]/div/div[1]/div[3]/button')
        navigate = browser.find_element_by_xpath((
            '//*[@id=\"inventory_container\"]/div/div[{0}]/div[3]/button').format(
            randomNumber))
        time.sleep(5)
        navigate.send_keys(Keys.ENTER)
        time.sleep(5)
        navigate.send_keys(Keys.RETURN)
        time.sleep(5)

# implement in another step]
# add validation,
