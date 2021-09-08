from selenium.webdriver.common.by import By


class AccountPageLocators:
    USER_MENU_ACCOUNT = (By.ID, "actionmenuaction-1")
    ADMINISTRATION_BUTTON = (By.XPATH, "//span[text()='Администрирование']")
    ADMINISTRATION_HEADER = (By.XPATH, "//a[@href='#linkroot']")
