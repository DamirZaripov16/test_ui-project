from locators.authentication import AuthenticationPageLocators


class AuthenticationPage:

    def __init__(self, app):
        self.app = app

    def authenticate(self, username: str, password: str):
        sign_in = self.app.driver.find_element(*AuthenticationPageLocators.SIGN_IN)
        sign_in.click()
        username_input = self.app.driver.find_element(*AuthenticationPageLocators.USERNAME)
        username_input.send_keys(username)
        password_input = self.app.driver.find_element(*AuthenticationPageLocators.PASSWORD)
        password_input.send_keys(password)
        submit_button = self.app.driver.find_element(*AuthenticationPageLocators.LOGIN_SUBMIT)
        submit_button.click()
