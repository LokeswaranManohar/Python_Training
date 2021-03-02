import pytest
import selenium.webdriver
import json


@pytest.fixture
def config(scope='session'):
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)  # function returns True if the specified object is of the
    # specified type, otherwise False
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


#########
# def browser():
#     # Initialize the ChromeDriver instance
#     b = selenium.webdriver.Chrome()
#
#     # Make its calls wait up to 10 seconds for elements to appear
#     b.implicitly_wait(10)
#
#     # Return the WebDriver instance for the setup
#     yield b
#
#     # Quit the WebDriver instance for the cleanup
#     b.quit()

@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()

    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()

    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)

    # ChromeOptions options = new ChromeOptions();
    # options.addArguments("disable-infobars");
    # ChromeDriver driver = new ChromeDriver(options);

    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
