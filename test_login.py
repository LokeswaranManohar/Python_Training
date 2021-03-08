import pytest
import time
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver

scenarios('../features/login.feature')


@then('move and validate result page')
def result(browser):
    browser.current_url
    time.sleep(5)