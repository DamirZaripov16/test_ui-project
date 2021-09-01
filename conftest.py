import logging

import pytest as pytest
from selenium.webdriver.chrome.options import Options

from models.authenticate import AuthenticationData
from pages.application import Application
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

logger = logging.getLogger("moodle")


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


@pytest.fixture
def authorize(app, request):
    user = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_authentication_page()
    data = AuthenticationData(username=user, password=password)
    app.authentication_page.authorize(data)


@pytest.fixture(scope='session')
def app(request):
    url = request.config.getoption("--url")
    logger.info(f"Start moodle {url}")
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    app = Application(webdriver.Chrome(ChromeDriverManager().install(),
                                       options=chrome_options), url,)
    yield app
    app.quit()
