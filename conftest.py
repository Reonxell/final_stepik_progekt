import pytest
from selenium.webdriver import FirefoxProfile
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser(request):
    language = request.config.getoption('--language')
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = Chrome(options=options)
    elif browser == 'firefox':
        fp = FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        driver = Firefox(firefox_profile=fp)

    def destroy():
        driver.quit()

    request.addfinalizer(destroy)
    return driver


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en")
    parser.addoption("--browser", action="store", default="chrome")
