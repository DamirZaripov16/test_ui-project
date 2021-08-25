from selenium.webdriver.common.by import By


class AuthenticationPageLocators:
    SIGN_IN = (By.XPATH, "/html/body/div[2]/nav/ul[2]/li[2]/div/span/a")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_SUBMIT = (By.ID, "loginbtn")
    # ACCOUNT_NAME = (By.CLASS_NAME, "account")