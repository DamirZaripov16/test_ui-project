import pytest as pytest
from selenium.webdriver.chrome.options import Options

from pages.application import Application
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption("--url",
                     action="store",
                     default="https://qacoursemoodle.innopolis.university",
                     help="Innopolis University Courses site url"),

    parser.addoption("--username",
                     action="store",
                     default="zaripov.damir@test.ru",
                     help="enter username"),

    parser.addoption("--password",
                     action="store",
                     default="Sharif1992*",
                     help="enter the password")


@pytest.fixture(scope='session')
def app(request):
    url = request.config.getoption("--url")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    app = Application(webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options), url,)
    yield app
    app.quit()
