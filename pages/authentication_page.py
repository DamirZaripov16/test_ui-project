import logging

from selenium.webdriver.remote.webelement import WebElement

from locators.base_page_locators import BasePageLocators
from models.authenticate import AuthenticationData
from pages.base_page import BasePage
from locators.authentication_page_locators import AuthenticationPageLocators
from locators.personal_data_page_locators import PersonalDataPageLocators


logger = logging.getLogger("moodle")


class AuthenticationPage(BasePage):
    def is_authorized(self):
        self.find_element(AuthenticationPageLocators.FORM)
        element = self.find_elements(AuthenticationPageLocators.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    def confirm_exit_window(self):
        self.find_element(AuthenticationPageLocators.FORM)
        element = self.find_elements(BasePageLocators.CONFIRM_EXIT_BUTTON)
        if len(element) > 0:
            return True
        return False

    def username_input(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.LOGIN)

    def password_input(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.PASSWORD)

    def submit_button(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.SUBMIT)

    def user_menu(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.USER_MENU)

    def exit(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.EXIT)

    def confirm_exit(self):
        return self.find_element(BasePageLocators.CONFIRM_EXIT_BUTTON)

    def authorize(self, data: AuthenticationData):
        logger.info(f'Username is: "{data.username}, password is: {data.password}"')
        if self.is_authorized():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        if self.confirm_exit_window():
            self.click_element(self.confirm_exit())
        self.fill_element(self.username_input(), data.username)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def log_out(self):
        if self.is_authorized():
            self.click_element(self.user_menu())
            self.click_element(self.exit())

    def user_menu_settings(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.USER_MENU_SETTINGS)

    def go_to_editing_personal_data(self):
        self.click_element(self.user_menu())
        self.click_element(self.user_menu_settings())
        self.click_element(self.find_element(PersonalDataPageLocators.EDIT_INFO))

    def authentication_login_error(self) -> str:
        return self.find_element(AuthenticationPageLocators.LOGIN_ERROR).text

    def go_to_sign_up_page(self):
        self.click_element(self.sign_up_button())

    def sign_out(self):
        if self.is_authorized():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        if self.confirm_exit_window():
            self.click_element(self.confirm_exit())

    def sign_up_button(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.SIGN_UP_BUTTON)
