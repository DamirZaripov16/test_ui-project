from selenium.webdriver.remote.webelement import WebElement

from models.authenticate import AuthenticationData
from pages.base_page import BasePage
from locators.authentication_page_locators import AuthenticationPageLocators
from locators.personal_data_page_locators import PersonalDataPageLocators


class AuthenticationPage(BasePage):

    def is_authorized(self):
        self.find_element(AuthenticationPageLocators.FORM)
        element = self.find_elements(AuthenticationPageLocators.USER_BUTTON)
        if len(element) > 0:
            return True
        return False

    def username_input(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.USERNAME)

    def password_input(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.PASSWORD)

    def submit_button(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.LOGIN_SUBMIT)

    def user_menu(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.USER_MENU)

    def exit(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.EXIT)

    def authorize(self, data: AuthenticationData):
        if self.is_authorized():
            self.click_element(self.user_menu())
            self.click_element(self.exit())
        self.fill_element(self.username_input(), data.username)
        self.fill_element(self.password_input(), data.password)
        self.click_element(self.submit_button())

    def log_out(self):
        if self.is_authorized():
            self.click_element(self.user_menu())
            self.click_element(self.exit())

    def log_out_check(self):
        return self.find_element(AuthenticationPageLocators.LOG_OUT_CHECK).text

    def user_menu_settings(self) -> WebElement:
        return self.find_element(AuthenticationPageLocators.USER_MENU_SETTINGS)

    def go_to_editing_personal_data(self):
        self.click_element(self.user_menu())
        self.click_element(self.user_menu_settings())
        self.click_element(self.find_element(PersonalDataPageLocators.EDIT_INFO))

    def authentication_login_error(self) -> str:
        return self.find_element(AuthenticationPageLocators.LOGIN_ERROR).text
