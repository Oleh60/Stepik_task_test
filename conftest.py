import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser1 = webdriver.Chrome("C:\\CD\\chromedriver.exe")
#     browser1.maximize_window()
#     browser1.implicitly_wait(8)
#     yield browser1
#     print("\nquit browser..")
#     browser1.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: uk or es ....others")

#
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome("C:\\CD\\chromedriver.exe", options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()