from selenium.webdriver.common.by import By


class AuthenticationPageLocators:
    SIGN_IN = (By.LINK_TEXT, "Вход")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_SUBMIT = (By.ID, "loginbtn")
    # ACCOUNT_NAME = (By.CLASS_NAME, "account")