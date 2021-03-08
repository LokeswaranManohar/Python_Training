import pytest
import time
import random
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

scenarios('../features/check.feature')


@then('in result page click on random item')
def result(browser):
    currenturl = browser.current_url
    randomNumber = random.randint(1, 6)
    if currenturl == 'https://www.saucedemo.com/inventory.html':
        # navigate = browser.find_element_by_xpath('//*[@id="inventory_container"]/div/div[1]/div[3]/button')
        navigate = browser.find_element_by_xpath((
            '//*[@id=\"inventory_container\"]/div/div[{0}]/div[3]/button').format(
            randomNumber))
        time.sleep(2)
        navigate.send_keys(Keys.ENTER)
        time.sleep(2)


@then('move to cart page')
def cart(browser):
    browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[3]/a").click()
    time.sleep(2)


@then('click on checkout')
def cart(browser):
    browser.find_element_by_link_text('CHECKOUT').send_keys(Keys.ENTER)
    time.sleep(2)
