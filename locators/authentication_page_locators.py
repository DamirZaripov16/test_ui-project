from selenium.webdriver.common.by import By


class AuthenticationPageLocators:
    SIGN_IN = (By.XPATH, "/html/body/div[2]/nav/ul[2]/li[2]/div/span/a")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_SUBMIT = (By.ID, "loginbtn")
    # ACCOUNT_NAME = (By.CLASS_NAME, "account")



    FORM = (By.ID, "page-wrapper")
    USER_BUTTON = (By.CLASS_NAME, "userbutton")
    USER_MENU = (By.CLASS_NAME, "usermenu")
    EXIT = (By.ID, "actionmenuaction-6")
    LOGIN_ERROR = (By.ID, "loginerrormessage")