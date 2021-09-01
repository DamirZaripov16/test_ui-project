import logging

from pages.authentication_page import AuthenticationPage
from pages.personal_data_page import PersonalDataPage

logger = logging.getLogger("moodle")


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.authentication_page = AuthenticationPage(self)
        self.personal_data = PersonalDataPage(self)

    def open_main_page(self):
        logger.info(f'Opening"{self.url}"')
        self.driver.get(self.url)

    def open_authentication_page(self):
        logger.info(f'Opening authentication page')
        self.driver.get(self.url + "/login/index.php")

    def quit(self):
        self.driver.quit()
