import logging

from pages.authentication_page import AuthenticationPage
from pages.sign_up_page import SignUpPage

from pages.personal_data_page import (
    PersonalDataPage,
    PersonalDataPageMore,
    PersonalDataPageOptional,
    PersonalDataPageTag,
)

logger = logging.getLogger("moodle")


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.authentication_page = AuthenticationPage(self)
        self.personal_data = PersonalDataPage(self)
        self.sign_up_page = SignUpPage(self)
        self.personal_data_more = PersonalDataPageMore(self)
        self.personal_data_optional = PersonalDataPageOptional(self)
        self.personal_data_tag = PersonalDataPageTag(self)

    def open_main_page(self):
        logger.info(f'Opening"{self.url}"')
        self.driver.get(self.url)

    def open_authentication_page(self):
        logger.info(f'Opening "{self.url}/login/index.php" - authentication page')
        self.driver.get(self.url + "/login/index.php")

    def quit(self):
        self.driver.quit()
