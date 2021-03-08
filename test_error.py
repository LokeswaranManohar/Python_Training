import pytest
import time
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

scenarios('../features/login_error.feature')


@then('validate the error message')
def error(browser):
    message = browser.find_element_by_xpath('//*[@id="login_button_container"]/div/form/h3')
    assert message.text == "Epic sadface: Sorry, this user has been locked out."

