# from locators.authentication_page_locators import AuthenticationPageLocators
#
#
# class AuthenticationPage:
#
#     def __init__(self, app):
#         self.app = app
#
#     def authenticate(self, username: str, password: str):
#         sign_in = self.app.driver.find_element(*AuthenticationPageLocators.SIGN_IN)
#         sign_in.click()
#         username_input = self.app.driver.find_element(*AuthenticationPageLocators.USERNAME)
#         username_input.send_keys(username)
#         password_input = self.app.driver.find_element(*AuthenticationPageLocators.PASSWORD)
#         password_input.send_keys(password)
#         submit_button = self.app.driver.find_element(*AuthenticationPageLocators.LOGIN_SUBMIT)
#         submit_button.click()


from selenium.webdriver.remote.webelement import WebElement

from models.authenticate import AuthenticationData
from pages.base_page import BasePage
from locators.authentication_page_locators import AuthenticationPageLocators


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

    def authentication_login_error(self) -> str:
        return self.find_element(AuthenticationPageLocators.LOGIN_ERROR).text
