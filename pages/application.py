from pages.authentication_page import AuthenticationPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.authentication_page = AuthenticationPage(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def open_authentication_page(self):
        self.driver.get(self.url + "/login/index.php")

    def quit(self):
        self.driver.quit()
