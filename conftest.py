import logging

import pytest as pytest
from selenium.webdriver.chrome.options import Options

from models.authenticate import AuthenticationData
from pages.application import Application
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

logger = logging.getLogger("moodle")


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="enter 'true' if you want to run the tests in headless mode,\n"
        "enter 'false' - if not",
    ),
    parser.addoption(
        "--url",
        action="store",
        default="https://qacoursemoodle.innopolis.university",
        help="Innopolis University Courses site url",
    ),

    parser.addoption(
        "--username",
        action="store",
        default="zaripov.damir@test.ru",
        help="enter username",
    ),

    parser.addoption(
        "--password", action="store", default="Sharif1992*", help="enter the password"
    )


@pytest.fixture
def authorize(app, request):
    user = request.config.getoption("--username")
    password = request.config.getoption("--password")
    app.open_authentication_page()
    data = AuthenticationData(username=user, password=password)
    app.authentication_page.authorize(data)
    assert app.authentication_page.is_authorized(), "You are not in!"
    yield
    app.authentication_page.sign_out()


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--url")
    headless_mode = request.config.getoption("--headless").lower()
    logger.info(f"Start moodle {url} with headless={headless_mode} mode")
    logger.info(f"Start moodle {url}")
    if headless_mode == "true":
        chrome_options = Options()
        chrome_options.headless = True
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options),
            url,
        )
    elif headless_mode == "false":
        fixture = Application(
            webdriver.Chrome(ChromeDriverManager().install()),
            url,
        )
    else:
        raise pytest.UsageError("--headless should be true or false")
    yield fixture
    fixture.quit()
