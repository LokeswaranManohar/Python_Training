import pytest
from selenium import webdriver
from pytest_bdd import given, when
import time

SwagLabs_Home = 'https://www.saucedemo.com/'


@pytest.fixture
def browser():
    browse = webdriver.Chrome()
    browse.implicitly_wait(10)
    yield browse
    browse.quit()


@given('the SwagLabs home page is displayed')
def swag_home(browser):
    browser.get(SwagLabs_Home)
    browser.maximize_window()


@when('the user type "<username>"')
def search_user(browser, username):
    browser.find_element_by_name('user-name').send_keys(username)
    time.sleep(2)


@when('the user type "<password>"')
def search_pas(browser, password):
    browser.find_element_by_name('password').send_keys(password)
    time.sleep(2)


@when('the user click login')
def login(browser):
    browser.find_element_by_id('login-button').click()
